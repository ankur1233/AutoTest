#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan Xin
#2020-02-07
import os
import sys
import unittest
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\Interface')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Interface import Interface
import GlobalVariable
import Common

class InterfaceTest(unittest.TestCase):
    def setUp(self):
        self.interface = Interface.Interface()
        self.t = round(time.time())
        self.logger = Common.case_log('Interface')[0]
        self.mysql = Common.OpreationMysql()
    def tearDown(self):
        pass

    def test1opendoor(self):  # 向中控发起开门指令
        try:
            url = 'http://%s:9999/api/faceEvent' % (GlobalVariable.IP['中控'])
            data = {"deviceId": 'null',
                    "idcard": "622923198502010039",   # 只需身份证正确即可开门
                    "name": "gj",
                    "path": "/storage/emulated/0/Android/data/com.cnksi.face/face/facePic/870902881207816192.png",
                    "time": self.t}
            self.logger.info('准备向中控发起开门指令')
            self.logger.info('url: ' + url)
            self.logger.info('data: ' + str(data))
            res = self.interface.post(url, data)
            self.assertIn(200, res.text, '开门接口正常')
            self.logger.info('开门接口正常：' + str(res.text))
        except BaseException as b:
            self.logger.error('开门接口异常：' + str(b))
            raise b

    def test2closedoor(self):  # 向中控发起关门指令
        try:
            url = 'http://%s:9999/api/closeDoor' % (GlobalVariable.IP['中控'])
            self.logger.info('准备向中控发起关门指令')
            self.logger.info('url: ' + url)
            res  =self.interface.get(url=url)
            self.assertIn(200,res.text, '关门接口正常')
            self.logger.info('开门接口正常' + str(res.text))
        except BaseException as b:
            self.logger.error('关门接口异常：' + str(b))
            raise b

    def test3toSafetyRiskManager(self):  # 安全风险管控大屏获取数据接口
        try:
            workid = 3
            url = 'http://%s/nwTool/getWorkUseTool?WorkId=%d' % (GlobalVariable.WebLogin["url"], workid)
            self.logger.info('准备向后台请求信息')
            self.logger.info('url: ' + url)
            res = self.interface.get(url=url)
            self.assertIn(200, res.text, '数据请求接口正常')
            self.logger.info('数据请求接口正常' + str(res.text))
        except BaseException as b:
            self.logger.error('数据请求接口异常：' + str(b))
            raise b

    def test4GsTwoBills(self):  # 甘肃两票推送接口
        try:
            self.mysql.connect_db()
            category = '验电器'
            storeroom = '750kV兰州东变电站'
            person_name = ['王珂', '段然']  # 工作票人物
            sql = "select `name`,`serial`,`category`,`rfid`,`dept_name`,`enabled` FROM `nw_tool` where " \
                  "dept_name='%s' and category like'%%s' and enabled=0;" % (category, storeroom)
            tool = self.mysql.select(sql)
            tool_list = []  # 初始化一个工器具列表，参数传入会用
            sql1 =["select `id`,`uaccount`,`idcard`,`dname`,`uname` from k_usr where `uname`=%s and `enabled`=0 " \
                  "and `dname`=%s" % (i, storeroom) for i in person_name]
            person = [self.mysql.select(k) for k in sql1]
            person_name.clear()
            #tool= (('35kV验电器', 'GDY-Ⅱ', '验电器', '750kV兰州东变电站', '0'),
            # ('35kV验电器', 'GDY-Ⅱ', '验电器', '750kV兰州东变电站', '0'),
            # ('66kV验电器', 'GDY', '验电器', '750kV兰州东变电站', '0'),
            # ('66kV验电器', 'GDY', '验电器', '750kV兰州东变电站', '0'),
            # ('330kV验电器', 'GDY－Ⅱ－330', '验电器', '750kV兰州东变电站', '0'),
            # ('330kV验电器', 'GDY', '验电器', '750kV兰州东变电站', '0'))
            url = '%s/nwTool/api/saveToolsInfo' % (GlobalVariable.WebLogin["url"])
            data = {"content": { "work_sheet_id": Common.current_stamp,
                                 "plan_start_time": Common.current_date,
                                 "plan_end_time": Common.current_date,
                                 "tool_list":[tool_list.append({"tool_name":i[0],
                                                                "tool_model": i[1],
                                                                "category": i[2],
                                                                "tool_rfid": i[3]}) for i in tool],
                                 "work_content": "任务-%s" % (Common.current_date),
                                 "sheet_no": Common.current_stamp - 1,
                                 "user_ids": [{"id": j[0],
                                               "uaccount": j[1]} for j in person],
                                 "accept_person_id": [{"id": j[0],
                                               "uaccount": j[1]} for j in person]
                                 }
                    }
            self.logger.info("url: " + url)
            self.logger.info("data: " + str(data))
            res = self.interface.post(url,data)
            self.assertIn("添加成功", res.text, "甘肃工作票接口正常")
            self.logger.info('甘肃工作票接口正常' + str(res.text))
        except BaseException as b:
            self.logger.error("甘肃工作票接口异常" + str(b))
            raise b

    def test5NcRuiNong(self):  # 南充瑞隆推送工作票接口
        try:

        except BaseException as b:
            self.logger.error('瑞隆任务接口异常： ' + str(b))
            raise b
if __name__ == '__main__':
    unittest.main()


