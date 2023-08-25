from flask import Flask, jsonify
from sqlalchemy import create_engine
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
    try:
        houses = []
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


if __name__ == '__main__':
    app.run()
