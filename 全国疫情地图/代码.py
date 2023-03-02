import json
from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

# 读取数据文件
f = open('疫情.txt', 'r', encoding='utf-8')
data = f.read()
# 关闭文件
f.close()
# 取到各省数据
# 将字符串json转换为python的字典
data_dict = json.loads(data)
# 从字典中取出省份的数据
province_data_list = data_dict['areaTree'][0]['children']
# 组装每个省和确诊人数为元组，并各个省的数据都封装入列表
data_list = []

special_administrative_region=['香港','澳门']
autonomous_region=['内蒙古自治区','宁夏回族自治区','新疆维吾尔自治区','西藏自治区','广西壮族自治区']
shi=['北京','天津','上海','重庆']
print(province_data_list)
for province_data in province_data_list:
    if province_data['name'] in shi:
        province_name = province_data['name'] + '市'
    elif province_data['name'] in special_administrative_region:
        province_name = province_data['name'] + '特别行政区'
    elif province_data['name'] in autonomous_region:
        province_name = province_data['name']
    else:
        province_name = province_data['name']+'省'  # 省份名称
    province_confirm = province_data['total']['confirm']  # 确诊人数
    data_list.append((province_name, province_confirm))

# 创建地图对象
map = Map()
# 添加数据
map.add('各省份确诊人数', data_list, 'china')
# 设置全局变量
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1,"max": 99,"lable":"1~99人","color":"#CCFFFF"},
            {"min": 100,"max": 999,"lable": "100~9999人","color":"#FFFF99"},
            {"min": 1000,"max": 4999,"lable":"1000~4999人","color":"#FF9966"},
            {"min": 5000,"max": 9999,"lable":"5000~99999人","color":"#FF6666"},
            {"min": 10000,"max": 99999,"lable":"10000~99999人","color":"#CC3333"},
            {"min": 100000,"lable": "100000+","color":"#990033"}
        ]
    )
)
# 绘图
map.render('全国疫情地图.html')
