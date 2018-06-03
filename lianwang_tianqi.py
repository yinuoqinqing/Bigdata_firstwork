# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:50:37 2018
应用其他工具包：import 包名
网络资源地址简称：URL
@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

#json(dict)格式工具包
import json
data=json.loads(info)

city=data['name']
print("当前城市"+str(city))

temp=data['main']['temp']
print(temp)

tempmax=data['main']['temp_max']
print("最高温度:"+str(tempmax))

pressure=data['main']['pressure']
print("气压:"+str(pressure))

description=data['weather'][0]['description']
print("当前天气状况:"+description)














