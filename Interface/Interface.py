#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan Xin
#2020-02-07

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+r'\venv\Lib\site-packages\\')
import requests
import json
class Interface:
    def __init__(self):
        self.header = {"Content-Type": 'application/json'}

    def post(self, url, data):
        postres = None
        postres = requests.post(url=url, json=data, headers=self.header)
        return postres

    def get(self, url, data=None):
        getres = None
        getres = requests.post(url=url, json=data, headers=self.header)
        return getres



if __name__ == '__main__':
    data1 = {"deviceId": 'null',
             "idcard": "622923198502010039",
             "name": "gj",
             "path": "/storage/emulated/0/Android/data/com.cnksi.face/face/facePic/870902881207816192.png",
             "time": 371477924}
    data2 = {"content": {
             "work_sheet_id": 3,
             "plan_start_time": "2020-03-11",
             "plan_end_time": "2020-03-12",
             "tool_list": [
                 {
                     "tool_name": "35kV验电器",
                     "tool_model": "GDY-Ⅱ",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001070"
                 },
                 {
                     "tool_name": "35kV验电器",
                     "tool_model": "GDY-Ⅱ",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001071"
                  },
                 {
                     "tool_name": "66kV验电器",
                     "tool_model": "GDY",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001072"
                 },
                 {
                     "tool_name": "66kV验电器",
                     "tool_model": "GDY",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001073"
                 },
                 {
                     "tool_name": "330kV验电器",
                     "tool_model": "GDY－Ⅱ－330",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001074"
                 },
                 {
                     "tool_name":"330kV验电器",
                     "tool_model": "GDY",
                     "category": "验电器",
                     "tool_rfid": "730000750000000000001075"
                 }
             ],
             "work_content": "诗城变电检修",
             "sheet_no": "12231",
             "user_ids": [
                 {
                     "id": "820804009902604288",
                     "uaccount": "27401253"
                 }
            ],
            "accept_person_id": [
                 {
                     "id": "820804009902604288",
                     "uaccount": "27401253"
                  }
            ]
        }
        }
print(Interface().get(r'http://172.16.18.150:8080/safety_tools/nwTool/getWorkUseTool?WorkId=2').text)
