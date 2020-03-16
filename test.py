# coding=utf-8
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# url="http://192.168.163.129:8080/safety_tools/login.html"
# driver=webdriver.Chrome()
# driver.get(url)
# time.sleep(2)
# driver.find_element(By.XPATH,'//*[@id="j_username"]').send_keys(123)

# import sys
# D={"aa":12}
# print(D["aa"])
# d=('xpath',"11")
# def aa(loc):
#     print(sys._getframe().f_code.co_name)
# aa(d)
# import os
# print(os.path.abspath('2020-03-02logs.log'))
# import datetime
# import time,os
# todaty=datetime.datetime.now()
# offset = datetime.timedelta(days=-7)
# print(datetime.datetime.now())
# print(time.time())
# print(time.mktime((todaty + offset).timetuple()))
# print(os.path.getmtime('D:\PythonProject\AutoTest\logs'))
# 2020-03-09 17:48:10.120120
# 1583747290.12012
# 1583142490.0
# 1583575475.3016417
# import requests
# import json
# header = {}
# header["Content-Type"] = 'application/json'
# data = {"deviceId":'null',
#         "idcard":"622923198502010039",
#         "name":"gj",
#         "path":"/storage/emulated/0/Android/data/com.cnksi.face/face/facePic/870902881207816192.png",
#         "time":371477924}
# res = requests.post('http://192.168.8.10:9999/api/faceEvent', json=data, headers=header)
# print(res.text)
# print(res.status_code)
# res.json()


# tool = (('35kV验电器', 'GDY-Ⅱ', '验电器', '750kV兰州东变电站', '0'),('66kV验电器', 'GDY', '验电器', '750kV兰州东变电站', '0'))
# print(tool[1][1])
# tool_list = []
# [tool_list.append({"tool_name":i[0],"tool_model": i[1],"category": i[2],"tool_rfid": i[3]}) for i in tool]
# print(tool_list)
person_name = ['王珂', '段然']  # 工作票人物
storeroom = '750kV兰州东变电站'
sql1 =["select `id`,`uaccount`,`idcard`,`dname`,`uname` from k_usr where `uname`=%s and `enabled`=0 and `dname`=%s" % (i, storeroom) for i in person_name]
print(sql1)