# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 14:50:39 2018
"地址":"北京海淀区xxx"
"手机号码":"15411451241"
"寄信人":"jre"
@author: lenovo
"""
msg={"地址":"北京海淀区xxx",
 "手机号码":"15411451241",
 "寄信人":"jre"}
 
print(msg["地址"])
print(msg['手机号码'])
print(msg['寄信人'])

#写一个字典类型，表示一个人的基本信息
#姓名，身高，年龄，性别

information={'姓名':'jre',
             '性别':'女',
             '身高':'165cm',
             '年龄':18}
print(information['姓名'])
print(information['性别'])
print(information['身高'])
print(information['年龄'])


xzhq={'name':'薛之谦',
      'song':['丑八怪','演员','暧昧','认真的雪'],
      '昵称':'woqian',
      '认识的人的年龄':['18','20','14','30','50']
      }

songs=xzhq['song']
print(songs)
print("歌曲总数"+str(len(songs)))

print(max(xzhq['认识的人的年龄']))

#通过字典定义一个天气预报，未来5天的天气List，未来5天的情况，今天星期几
#并且求出最高温度是多少

weather={"未来5天":['周日',
                 '周一',
                 '周二',
                 '周三',
                 '周四'],
         "未来5天天气情况":['阴转多云',
                     '多云',
                     '晴',
                     '阴',
                     '小雨'],
         "未来5天每天最高温度":['28摄氏度',
                       '26摄氏度',
                       '30摄氏度',
                       '26摄氏度',
                       '24摄氏度'],
        "今天天气详情":['周六',
                  '小雨转阴',
                  '26摄氏度']}


print(weather['未来5天'])
print(len(weather['未来5天']))

print(weather["未来5天每天最高温度"])
print("未来5天最高气温"+max(weather["未来5天每天最高温度"]))
print("今天"+str(weather['今天天气详情']))


weather['未来5天'][0]
            




