from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
#使用sqlalchemy创建二手房对象类，便于建表
class OldHouse(Base):

    __tablename__ = 'second-hand_houses'
    #类的属性，与二手房源相对应
    id = Column(Integer,primary_key=True,autoincrement=True)
    # 房源名
    name = Column(String(50))
    # 房源户型（室）
    house = Column(Integer)
    # 房源户型（厅）
    hall = Column(Integer)
    # 房源面积 m²
    area = Column(Float)
    # 房源所处层（高中低顶层）
    floor = Column(String(10))
    # 房源所在楼的层数（共几层）
    count_floor = Column(Integer)
    # 房源朝向
    toward = Column(String(10))
    # 房源年份（几几年建成）
    year = Column(String(4))
    # 房源中介人
    intermediary_agent = Column(String(5))
    # 房源开发商
    developers = Column(String(50))
    # 房源详细地址
    address = Column(String(200))
    # 房源地址备注（可以理解为是否有靠近地铁）
    remark = Column(String(200))
    # 房源总价（万元）
    total_price = Column(Float)
    # 房源每平米价格 元/m²
    price = Column(Integer)
    # 详情页链接
    link = Column(String(200))

    #构造器
    def __init__(self,name,house,hall,area,floor,count_floor,toward,
                 year,intermediary_agent,developers,address,remark,total_price,price,link):
        self.name = name
        self.house = house
        self.hall = hall
        self.area = area
        self.floor = floor
        self.count_floor = count_floor
        self.toward = toward
        self.year = year
        self.intermediary_agent = intermediary_agent
        self.developers = developers
        self.address = address
        self.remark = remark
        self.total_price = total_price
        self.price = price
        self.link = link


