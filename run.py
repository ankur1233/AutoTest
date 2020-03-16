#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan xin 
#2020-03-02
import unittest
import sys
import os
import GlobalVariable
sys.path.append(os.path.abspath(__file__)+r'\venv\Lib\site-packages\\')
sys.path.append(os.path.abspath(__file__)+r'\venv\Lib\site-packages\\')
import Common
from HTMLTestRunner import HTMLTestRunner

Common.backup_log()  # 自动化开始前备份上次的日志文件
all_test = unittest.defaultTestLoader.discover(GlobalVariable.Path["webcases_path"], 'T*.py')
test_suit = unittest.TestSuite()
test_suit.addTests(all_test)
if os.path.exists(GlobalVariable.Path['report_path']) == 0:
    os.mkdir(GlobalVariable.Path['report_path'])
with open(GlobalVariable.Path['report_path'] + 'report.html', 'w', encoding='utf-8') as fp:
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有用例')
    runner.run(test_suit)
