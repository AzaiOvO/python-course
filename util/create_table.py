from sqlalchemy import create_engine
from Config.mysql_config import connection
from Model.oldHouse import Base


#创建数据库表
try:
    engine = create_engine(connection)
    Base.metadata.create_all(engine,checkfirst=True)
except Exception as e:
    print("建表失败！")