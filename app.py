from flask import Flask, jsonify,request
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
import json

from Model.oldHouse import OldHouse
from Config import mysql_config
from util.class2dict import oldhouse2dict

app = Flask(__name__)

engine = create_engine(mysql_config.connection)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/')
def hello_world():  # put application's code here
    return

#从数据库获取数据展示到前端列表
@app.route('/list')
def list():
    houses = []
    try:
        old_houses = session.query(OldHouse).all()
        #python对象需转换位json格式与前端交互
        for house in old_houses:
            #先将房源对象转为字典存储
            house = oldhouse2dict(house)
            # 字典转为json格式,设置ensure_ascii=False防止编译中文
            new_house = json.dumps(house,ensure_ascii=False)
            houses.append(new_house)
        houses = json.dumps(houses,ensure_ascii=False)
    except:
        return jsonify(code=11, message='query fail')
    if(houses is None):
        return jsonify(code=11, message='query fail')
    return houses

#从数据库获取面积相关统计数据送到前端
@app.route('/area')
def area():
    #使用字典存储数据
    data= {'below_50':0,
           'a50-70':0,
           'a70-90':0,
           'a90-110':0,
           'a110-130': 0,
           'a130-150': 0,
           'a150-200': 0,
           'up_200': 0,}
    try:
        #房源面积50平米以下的数量
        data['below_50'] = session.query(OldHouse).filter(OldHouse.area <= 50).count()
        data['a50-70'] = session.query(OldHouse).filter(OldHouse.area > 50).filter(OldHouse.area <= 70).count()
        data['a70-90'] = session.query(OldHouse).filter(OldHouse.area > 70).filter(OldHouse.area <= 90).count()
        data['a90-110'] = session.query(OldHouse).filter(OldHouse.area > 90).filter(OldHouse.area <= 110).count()
        data['a110-130'] = session.query(OldHouse).filter(OldHouse.area > 110).filter(OldHouse.area <= 130).count()
        data['a130-150'] = session.query(OldHouse).filter(OldHouse.area > 130).filter(OldHouse.area <= 150).count()
        data['a150-200'] = session.query(OldHouse).filter(OldHouse.area > 150).filter(OldHouse.area <= 200).count()
        data['up_200'] = session.query(OldHouse).filter(OldHouse.area > 200).count()
    except:
        return jsonify(code=11, message='query fail')
    return json.dumps(data,ensure_ascii=False)

#从数据库获取户型（室）相关统计数据送到前端
@app.route('/house')
def house():
    #使用字典存储数据
    data= {'s1':0,
           's2':0,
           's3':0,
           's4':0,
           's5': 0,
           's6': 0,
           's8': 0,}
    try:
        houses_count_sql = session.query(OldHouse.house, func.count(OldHouse.house)).group_by(OldHouse.house).all()
        #房源面积50平米以下的数量
        data['s1'] = houses_count_sql[0][1]
        data['s2'] = houses_count_sql[1][1]
        data['s3'] = houses_count_sql[2][1]
        data['s4'] = houses_count_sql[3][1]
        data['s5'] = houses_count_sql[4][1]
        data['s6'] = houses_count_sql[5][1]
        data['s8'] = houses_count_sql[6][1]
    except:
        return jsonify(code=11, message='query fail')
    return json.dumps(data,ensure_ascii=False)

#从数据库获取户型（所处层数）相关统计数据送到前端
@app.route('/floor')
def floor():
    #使用字典存储数据
    data= {'level_1':0,
           'level_2':0,
           'level_3':0,
           'level_4':0,
           'level_5': 0}
    try:
        floor_count_sql = session.query(OldHouse.floor, func.count(OldHouse.floor)).group_by(OldHouse.floor).all()
        #房源面积50平米以下的数量
        data['level_1'] = floor_count_sql[2][1]
        data['level_2'] = floor_count_sql[1][1]
        data['level_3'] = floor_count_sql[0][1]
        data['level_4'] = floor_count_sql[4][1]
        data['level_5'] = floor_count_sql[3][1]
    except:
        return jsonify(code=11, message='query fail')
    return json.dumps(data,ensure_ascii=False)

#从数据库获取建造年份及数量相关统计数据送到前端
@app.route('/year')
def year():
    #使用列表存储数据
    data = []
    try:
        #分年份获取数据
        results = session.query(OldHouse.year, func.count(OldHouse.year)).group_by(OldHouse.year).all()
        #封装
        for result in results:
            dict1 = {'year': '', 'count': 0}
            dict1['year'] = result[0]
            dict1['count'] = result[1]
            data.append(dict1)
    except:
        return jsonify(code=11, message='query fail')
    if data is None:
        return jsonify(code=11, message='no data')
    return json.dumps(data,ensure_ascii=False)

#从数据库获取每平价格相关统计数据送到前端
@app.route('/price')
def price():
    #使用字典存储数据
    data= {'below_1w':0,
           'w1_2':0,
           'w2_3':0,
           'w3_4':0,
           'w4_5': 0,
           'up_5w': 0}
    try:
        #房源面积50平米以下的数量
        data['below_1w'] = session.query(OldHouse).filter(OldHouse.price <= 10000).count()
        data['w1_2'] = session.query(OldHouse).filter(OldHouse.price > 10000).filter(OldHouse.price <= 20000).count()
        data['w2_3'] = session.query(OldHouse).filter(OldHouse.price > 20000).filter(OldHouse.price <= 30000).count()
        data['w3_4'] = session.query(OldHouse).filter(OldHouse.price > 30000).filter(OldHouse.price <= 40000).count()
        data['w4_5'] = session.query(OldHouse).filter(OldHouse.price > 40000).filter(OldHouse.price <= 50000).count()
        data['up_5w'] = session.query(OldHouse).filter(OldHouse.price > 50000).count()
    except:
        return jsonify(code=11, message='query fail')
    return json.dumps(data,ensure_ascii=False)

#从数据库获取每房源总价相关统计数据送到前端
@app.route('/total_price')
def total_price():
    #使用字典存储数据
    data= {'below_80w':0,
           'w80_100':0,
           'w100_120':0,
           'w120_150':0,
           'w150_200': 0,
           'w200_300': 0,
           'w300_500': 0,
           'up_500w': 0}
    try:
        #房源面积50平米以下的数量
        data['below_80w'] = session.query(OldHouse).filter(OldHouse.total_price <= 80).count()
        data['w80_100'] = session.query(OldHouse).filter(OldHouse.total_price > 80).filter(
            OldHouse.total_price <= 100).count()
        data['w100_120'] = session.query(OldHouse).filter(OldHouse.total_price > 100).filter(
            OldHouse.total_price <= 120).count()
        data['w120_150'] = session.query(OldHouse).filter(OldHouse.total_price > 120).filter(
            OldHouse.total_price <= 150).count()
        data['w150_200'] = session.query(OldHouse).filter(OldHouse.total_price > 150).filter(
            OldHouse.total_price <= 200).count()
        data['w200_300'] = session.query(OldHouse).filter(OldHouse.total_price > 200).filter(
            OldHouse.total_price <= 300).count()
        data['w300_500'] = session.query(OldHouse).filter(OldHouse.total_price > 300).filter(
            OldHouse.total_price <= 500).count()
        data['up_500w'] = session.query(OldHouse).filter(OldHouse.total_price > 500).count()
    except:
        return jsonify(code=11, message='query fail')
    return json.dumps(data,ensure_ascii=False)

#根据面积搜索房源
@app.route('/search_by_area', methods=['POST'])
def search_by_area():
    houses = []
    #获取前端post来的数据
    data = request.data
    #原数据格式为byte,因此需提取除其中的字典格式数据
    try:
        data = eval(data)
    except:
        return 'error'
    #两面积都为0，直接返回空
    if(data['area1'] == data['area2'] == 0):
        return 'error'
    else:
        try:
            old_houses = session.query(OldHouse).filter(OldHouse.area>=data['area1']).filter(OldHouse.area<=data['area2']).all()
            # python对象需转换位json格式与前端交互
            for house in old_houses:
                # 先将房源对象转为字典存储
                house = oldhouse2dict(house)
                # 字典转为json格式,设置ensure_ascii=False防止编译中文
                new_house = json.dumps(house, ensure_ascii=False)
                houses.append(new_house)
            houses = json.dumps(houses, ensure_ascii=False)
        except:
            return jsonify(code=11, message='query fail')
    if (houses is None):
        return jsonify(code=11, message='no data')
    return houses


#根据总价搜索房源
@app.route('/search_by_price', methods=['POST'])
def search_by_price():
    houses = []
    #获取前端post来的数据
    data = request.data
    #原数据格式为byte,因此需提取除其中的字典格式数据
    try:
        data = eval(data)
    except:
        return 'error'
    #两总价都为0，直接返回空
    if(data['price1'] == data['price2'] == 0):
        return 'error'
    else:
        try:
            old_houses = session.query(OldHouse).filter(OldHouse.total_price>=data['price1']).filter(OldHouse.total_price<=data['price2']).all()
            # python对象需转换位json格式与前端交互
            for house in old_houses:
                # 先将房源对象转为字典存储
                house = oldhouse2dict(house)
                # 字典转为json格式,设置ensure_ascii=False防止编译中文
                new_house = json.dumps(house, ensure_ascii=False)
                houses.append(new_house)
            houses = json.dumps(houses, ensure_ascii=False)
        except:
            return jsonify(code=11, message='query fail')
    if (houses is None):
        return jsonify(code=11, message='no data')
    return houses



if __name__ == '__main__':
    app.run()
