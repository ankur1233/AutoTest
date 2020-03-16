#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan xin 
#2020-02-07
import os
'''接口测试专用'''
'''WEBUI专用'''
step_excute_res = []  # 用例每一步执行结果，用于判断用例是否执行成功
case_excute_res = []  # 用例执行结果，用于重命名文件夹
GlobalPathSrc = os.path.dirname(os.path.abspath(__file__))  # 全局路径起始点
# 全局路径信息
Path = {"report_path": GlobalPathSrc + r"\report\\",  # 报告路径
        "error_log": GlobalPathSrc+r"\error.log",  # 工程运行错误日志
        "Immediate_path": GlobalPathSrc+r"\logs\\",  # 即时日志文件夹
        "webcases_path": GlobalPathSrc+r'\TestCasesWeb\\',  # web测试用例路径文件夹
        "executable_path": GlobalPathSrc+r"\venv\chromedriver.exe"  # 谷歌浏览器驱动路径
       }
#系统ip信息
IP = {"中控": "192.168.8.10",
      "后台": "172.16.18.150",
      "人脸": "192.168.8.111",
      "同步框架": "172.16.18.100",
      "MQ": "211.149.156.147",  # 推送服务器地址
      "数据库": "172.16.18.100"
      }
# 数据库连接信息
Mysql = {"host": IP["数据库"],
         "username": "root",
         "password": "wideal.cn",
         "port": "13306",
         "datebase": "gs_safety_tools"
         }
# 后台登录
WebLogin = {"url": "http://%s:8080/safety_tools" % (IP["后台"]),
            "web_province": {"account": "",
                             "password": ""},
            "web_city": {"account": "",
                         "password": ""},
            "web_country": {"account": "",
                            "password": ""},
            "web_group": {"account": "",
                          "password": ""}
            }
#  APP登录
ApkLogin = {"AppId": "gs_province_tools",
            "同步地址": "http://%s:8090/v411" % (IP["同步框架"]),
            "app_administrator": {"account": "",
                                  "password": ""},
            "app_member": {"account": "",
                           "password": ""}
            }
#  中控设置，"1"代表是,"0"代表否，
Control = {"IP":"",
           "AppId": "gs_province_rfid_tool",
           "Url": "http://%s:8090/v411" % (IP["同步框架"]),
           "人脸识别Url": "http://%s" % (IP["人脸"]),
           "中控功能密码":"wideal.cn",
           "允许离线运行": "0",
           "MqttUrl": "tcp://%s:1883" % (IP["MQ"]),
           "是否开启推送": "1",
           "品胜RFID": "1",
           "是否允许代领": "1",
           "最近计划": "15",
           "是否屏蔽Home": "1",
           "是否自动控制": "1",
           "是否空调加热": "1"
           }
#  人脸识别设置
Face = {"是否校验省份证合法": "1",
        "是否只能注册已登记人员": "1",
        "是否禁用导航栏": "1",
        "上报地址": "http://%s" % (IP["中控"]),
        "Appid": "gs_rfid_face",
        "同步地址": "http://%s:8090/v411" % (IP["同步框架"])
        }

if __name__ == '__main__':
    print(Face["上报地址"])