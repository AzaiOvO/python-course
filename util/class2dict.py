
#此文件用来储存将二手房源类转换成字典的方法
def oldhouse2dict(oldhouse):
    return {
        'id' : oldhouse.id,
        'name': oldhouse.name,
        'house': oldhouse.house,
        'hall': oldhouse.hall,
        'area': oldhouse.area,
        'floor': oldhouse.floor,
        'count_floor': oldhouse.count_floor,
        'toward': oldhouse.toward,
        'year': oldhouse.year,
        'intermediary_agent': oldhouse.intermediary_agent,
        'developers': oldhouse.developers,
        'address': oldhouse.address,
        'remark': oldhouse.remark,
        'total_price': oldhouse.total_price,
        'price': oldhouse.price,
        'link': oldhouse.link,

    }