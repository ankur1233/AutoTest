#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan xin 
#2020-02-07


import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\web')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+r'\venv\Lib\site-packages\\')
import time
import GlobalVariable
from OpreationLogin import LoginPage as LP
from selenium import webdriver
import Common


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.class_name = self.__class__.__name__
        self.current_path = os.path.abspath(__file__)
        fun_name = sys._getframe().f_code.co_name
        try:
            GlobalVariable.case_excute_res.append(self.class_name)  # 获取测试类名称
            GlobalVariable.case_excute_res.append(Common.current_date)  # 获取当前日期
            self.driver = webdriver.Chrome(GlobalVariable.Path["executable_path"])  # 设置谷歌驱动
            self.logger = Common.case_log('Web')[0]  # 实例化日志
            self.handler = Common.case_log('Web')[1]  # 实例化日志写入文件handler，
            self.LP = LP(self.driver, self.logger)  # 实例化网页操作
        except BaseException as b:
            Common.get_error(self.current_path, self.class_name, '初始化环境失败>>>', str(b))
            raise b

    def tearDown(self) -> None:
        fun_name = sys._getframe().f_code.co_name
        try:
            if 'False' not in GlobalVariable.step_excute_res and len(GlobalVariable.step_excute_res) != 0:
                GlobalVariable.case_excute_res.append('success')  # 执行结果列表所有步骤都为True则成功
            else:
                GlobalVariable.case_excute_res.append('Failed')  # 否则用例执行失败
            Common.save_log(GlobalVariable.case_excute_res)  # 将日志保存到用例日志文件夹
            Common.rename_caselog(GlobalVariable.case_excute_res)
            self.handler.close()  # 关闭日志写入文件句柄，释放线程锁，即可删除上一个用例生成的日志文件
            Common.del_file(GlobalVariable.Path["Immediate_path"] + GlobalVariable.case_excute_res[2])  # 删除日志文件
            self.handler._open()  # 重新打开日志写入文件句柄，以便下一个用例日志写入文件
            GlobalVariable.step_excute_res.clear()  # 重置测试步骤列表
            GlobalVariable.case_excute_res.clear()  # 重置测试结果列表
        except BaseException as b:
            Common.get_error()
            raise b
        finally:
            self.driver.quit()  # 关闭浏览器
    def testcase1(self):
        casename = sys._getframe().f_code.co_name
        self.logger.info("当前运行用例：" + casename)
        GlobalVariable.case_excute_res.append(casename)
        self.LP.open_web()
        self.LP.input_user('27401253')
        self.LP.input_password('1')
        self.LP.click_login()
        time.sleep(3)
        try:
            self.assertEqual(self.LP.get_title(), "后台管理系统!")
            GlobalVariable.step_excute_res.append('True')
            self.logger.info("测试通过")
        except AssertionError as a:
            self.logger.error("错误原因"+str(a))
            GlobalVariable.step_excute_res.append('False')
    def testcase2(self):
        casename = sys._getframe().f_code.co_name
        self.logger.info("当前运行用例：" + casename)
        GlobalVariable.case_excute_res.append(casename)
        self.LP.open_web()
        self.LP.input_user('27401253')
        self.LP.input_password('1')
        self.LP.click_login()
        time.sleep(3)
        try:
            self.assertEqual(self.LP.get_title(), "后台管理系统")
            GlobalVariable.step_excute_res.append('True')
            self.logger.info("测试通过")
        except AssertionError as a:
            self.logger.error("错误原因"+str(a))
            GlobalVariable.step_excute_res.append('False')


if __name__ == '__main__':
    unittest.main()
