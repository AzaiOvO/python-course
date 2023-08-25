import random
import time

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from lxml import etree
import re

from Model.oldHouse import OldHouse
from Config.mysql_config import connection

#请求头
headers = {
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
           }

# 目标网址
# url = 'http://127.0.0.1:5000/'

#处理换行符和制表符
def font_clean(str):
    str = str.replace('\t','')
    str = str.replace('\n', '')
    return str

#爬虫程序
def spider(url):
    # 初始化二手房对象列表为空
    oldHouses = []
    # 爬取页面源码数据
    page_text = requests.get(url=url, headers=headers).text
    # print(page_text)

    # 解析源码数据
    tree = etree.HTML(page_text)
    dls = tree.xpath('//div[contains(@class,"shop_list")]/dl[contains(@dataflag,"bg")]')

    for dl in dls:
        try:
            # 获取房源名称
            name = dl.xpath('./dd/h4/a/span/text()')[0]
            # 消除制表符干扰
            name = font_clean(name)

            # 获取房源户型：几室几厅
            size = dl.xpath('./dd/p[1]/text()')[0]
            size = font_clean(size)
            # size[0]室size[2]厅
            # 室和厅强制类型转换
            house = (int)(size[0])
            hall = (int)(size[2])
            # print(size)

            # 获取房源面积
            area = dl.xpath('./dd/p[1]/text()')[1]
            area = font_clean(area)
            area = area[:-1]
            # 面积强制类型转换
            area = (float)(area)
            # print(area[:-1])

            # 获取楼层
            floor = dl.xpath('./dd/p[1]/text()')[2]
            floor = font_clean(floor)
            # 楼层信息页面不一致，需要特殊处理
            if (len(floor) == 0):
                floor = dl.xpath('./dd/p[1]/a/text()')[0]
            # 统一楼层格式
            floor = floor[:2]
            # print(floor)

            # 获取所在楼的层数
            count_floor = dl.xpath('./dd/p[1]/text()')[3]
            count_floor = font_clean(count_floor)
            # 处理特殊数据
            if ("层" not in count_floor):
                count_floor = dl.xpath('./dd/p[1]/text()')[2]
                count_floor = font_clean(count_floor)
                count_floor = count_floor[2:]
            # 取数字即可
            count_floor = re.findall(r'\d+', count_floor)[0]
            # 强制类型转换
            count_floor = (int)(count_floor)
            # print(count_floor)

            # 初始化房源朝向、年份
            toward = ''
            year = ''
            infos = dl.xpath('./dd/p[1]/text()')
            for info in infos:
                # print(font_clean(info))
                if ("向" in info):
                    # 获取房源朝向
                    toward = font_clean(info)
                if ("年" in info):
                    # 获取房源年份
                    year = font_clean(info)
                    # 年份也int型强制转换
                    year = year[:-2]
            # print(toward + year)

            # 获取中介负责人
            intermediary_agent = dl.xpath('./dd/p[1]/span/a/text()')[0]
            # print(intermediary_agent)

            # 获取开发商
            developers = dl.xpath('./dd/p[2]/a/text()')[0]
            developers = font_clean(developers)
            # print(developers)

            # 获取详细地址
            address = dl.xpath('./dd/p[2]/span/text()')[0]
            # print(address)

            # 获取地址备注描述
            remarks = dl.xpath('./dd/p[3]/span[contains(@class,"bg_none icon_dt")]')
            # 处理备注描述可能为空的情况
            if (remarks):
                remark = remarks[0].xpath('./text()')[0]
            else:
                remark = ''
            # print(remark)

            # 获取房源价格，包括总价和每平价格
            total_price = dl.xpath('./dd[contains(@class,"price_right")]/span[1]/b/text()')[0]  # 总价
            total_price = (float)(total_price)
            price = dl.xpath('./dd[contains(@class,"price_right")]/span[2]/text()')[0]  # 每平米价格
            price = price[:-3]  # 只取数字
            price = (int)(price)
            # print(price)

            # 获取详情连接
            link = dl.xpath('./dd/h4/a/@href')[0]
            # print(link)

            # 封装
            oldHouse = OldHouse(name, house, hall, area, floor, count_floor, toward,
                                year, intermediary_agent,developers, address, remark, total_price, price, link)
            # print(oldHouse)
            oldHouses.append(oldHouse)
        except:
            continue
    print("爬取完成，本次共爬取%d条数据！" % len(oldHouses))
    return oldHouses

# 添加到数据库
def save_data(datas,connection):
    engine = create_engine(connection)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        for data in datas:
            session.add(data)
        print("添加数据成功！")
        session.commit()
    except Exception as e:
        print(e)
        print("添加失败,准备回滚！")
        session.rollback()

#处理翻页
def handle_url():
    #初始爬取的url
    base_url = "https://nanjing.esf.fang.com/house/i3"
    for i in range(30):
        url = base_url + str(i + 1) + '/'
        # 异步加载，需要再次获取url才能拿到数据
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        new_url = tree.xpath('//div[contains(@class,"redirect")]/a/@href')[0]
        print(new_url)
        houses = spider(new_url)
        save_data(datas=houses, connection=connection)
        #每次循环需要等待一段时间,此处设置随机等待10-20秒
        time.sleep(random.randint(10,20))


# houses = spider(url)
# save_data(datas=houses,connection=connection)

# handle_url()