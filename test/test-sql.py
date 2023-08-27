
from sqlalchemy import create_engine,func
from sqlalchemy.orm import sessionmaker

from Config import mysql_config
from Model.oldHouse import OldHouse

engine = create_engine(mysql_config.connection)
Session = sessionmaker(bind=engine)
session = Session()

#测试查询面积
# result = session.query(OldHouse).filter(OldHouse.area >= 50).filter(OldHouse.area <= 70).count()

#测试查询室
# result = session.query(OldHouse.house, func.count(OldHouse.house)).group_by(OldHouse.house).all()

#测试查询所在层
# result = session.query(OldHouse.floor, func.count(OldHouse.floor)).group_by(OldHouse.floor).all()

#测试查询建造年数及数量
# results = session.query(OldHouse.year, func.count(OldHouse.year)).group_by(OldHouse.year).all()

#测试查询每平价格(10000-20000)及数量
results = session.query(OldHouse).filter(OldHouse.price > 10000).filter(OldHouse.price <= 20000).count()
print(results)



# data = []
#
# for result in results:
#     dict1 = {'year': '', 'count': 0}
#     dict1['year'] = result[0]
#     dict1['count'] = result[1]
#     data.append(dict1)
# print(data)
