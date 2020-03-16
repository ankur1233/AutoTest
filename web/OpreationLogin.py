#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan Xin
#2020-02-28
from BaseActive import BaseActive as BA
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import time
import GlobalVariable
from selenium.webdriver.common.by import By


class LoginPage(BA):
    url = GlobalVariable.WebLogin["url"]  # 从GlobalVariable.py读取后台访问地址
    login_button = (By.XPATH, '//*[@id="login_ok"]')  # 登录按钮
    user_path = (By.XPATH, '//*[@id="j_username"]')  # 用户输入框
    psw_path = (By.XPATH, '//*[@id="j_password"]')  # 密码输入框
    def __init__(self, driver,logger):
        BA.__init__(self, driver)
        self.logger = logger  # 实例化日志模块

    def open_web(self):  # 打开网页操作

        try:
            self.logger.info("访问后台："+self.url)
            self.driver.maximize_window()  # 最大化浏览器
            time.sleep(2)
            self.driver.get(self.url)
            GlobalVariable.step_excute_res.append('True')
        except Exception as e:
            self.logger.error("访问后台错误："+str(e))
            GlobalVariable.step_excute_res.append('False')
            raise False

    def input_user(self, user):  # 输入用户名
        try:
            self.logger.info("输入用户名："+user)
            self.input_text(self.user_path, user)
            GlobalVariable.step_excute_res.append('True')
        except Exception as e:
            self.logger.error(e)
            GlobalVariable.step_excute_res.append('False')
            raise False

    def input_password(self, password):  # 输入密码
        try:
            self.logger.info("输入密码："+password)
            self.input_text(self.psw_path, password)
            GlobalVariable.step_excute_res.append('True')
        except Exception as e:
            self.logger.error(e)
            GlobalVariable.step_excute_res.append('False')
            raise False

    def click_login(self):  # 点击登录
        try:
            self.logger.info("点击登录")
            self.click_once(self.login_button)
            GlobalVariable.step_excute_res.append('True')
        except Exception as e:
            self.logger.error(e)
            GlobalVariable.step_excute_res.append('False')
            raise False

    def get_title(self):
        try:
            h = self.driver.current_window_handle
            self.driver.switch_to.window(h)
            self.logger.info("获取新页面标题")
            title = self.driver.title
            GlobalVariable.step_excute_res.append('True')
        except Exception as e:
            self.logger.error(e)
            GlobalVariable.step_excute_res.append('False')
            raise False
        return title


if __name__ == '__main__':
    pass
