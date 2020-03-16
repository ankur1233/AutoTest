#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan Xin
#2020-02-07

class BaseActive(object):
    def __init__(self, driver):
        self.driver = driver

    ##########################元素操作#######################################
    '''清空输入内容'''

    def clear_content(self, loc):
        self.driver.find_element(*loc).clear()

    '''提交表单'''

    def submit_form(self, loc):
        self.driver.find_element(*loc).submit()

    '''元素输入'''

    def input_text(self, loc, text):
        self.driver.find_element(*loc).send_keys(text)

    '''点击单个元素'''

    def click_once(self, loc):
        self.driver.find_element(*loc).click()

    '''点击多个元素'''

    def click_some(self, loc):
        self.driver.find_elements(*loc).click()

    '''获取元素文本'''

    def get_text(self, loc):
        return self.driver.find_element(*loc).text

    '''获取元素尺寸'''

    def get_size(self, loc):
        return self.driver.find_element(*loc).size

    '''获取属性值'''

    def get_attribute_value(self, loc, name):
        return self.driver.find_element(*loc).get_attribute(name)
##########################元素定位#######################################
#定位单个元素driver.find_element(*loc)
#定位多个元素driver.find_elements(*loc)
#二级定位driver.find_element(*loc[0]).find_element_by(*loc[1])
#获取网页titledriver.title
##########################浏览器操作#####################################
#打开浏览器driver.get(url)
#浏览器后退driver.back()
#浏览器前进driver.forward()
##########################弹框处理#######################################
#返回弹框文字driver.switch_to_alert().text
#接受现有弹框driver.switch_to_alert().accept()
#解散现有弹框driver.switch_to_alert().dismiss()
#发送内容到弹框driver.switch_to_alert().send_keys(text)
##########################执行JS代码#####################################
#执行js代码driver.execute_script(js)
##########################多窗口处理#######################################
#获取当前窗口句柄driver.current_window_handle
#获取所有窗口句柄driver.window_handles
#切换句柄driver.switch_to_window(handle)
##########################表单处理#######################################
#切换到指定表单driver.switch_to.frame()
#切换到最外层表单driver.switch_to.default_content()
#切换到上层表单driver.switch_to.parent_frame()
    ##########################鼠标操作#######################################
    # '''右击'''
    #
    # def right_click(self, loc):
    #     ActionChains(self.driver).context_click(self.driver.find_element(*loc)).perform()
    #
    # '''双击'''
    #
    # def click_twice(self, loc):
    #     ActionChains(self.driver).double_click(self.driver.find_element(*loc)).perform()
    #
    # '''拖动'''
    #
    # def move(self, loc):
    #     ActionChains(self.driver).drag_and_drop(self.driver.find_element(*loc)).perform()
    #
    # '''悬停'''
    #
    # def stop(self, loc):
    #     ActionChains(self.driver).move_to_element(self.driver.find_element(*loc)).perform()
    #
    # '''左击保持按下'''
    #
    # def keep_left_click(self, loc):
    #     ActionChains(self.driver).click_and_hold(self.driver.find_element(*loc)).perform()

    ##########################键盘操作#######################################
    # '''删除键'''
    #
    # def delete_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.BACK_SPACE)
    #
    # '''空格键'''
    #
    # def space_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.SPACE)
    #
    # '''制表键'''
    #
    # def table_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.TAB)
    #
    # '''回退键'''
    #
    # def esc_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.ESCAPE)
    #
    # '''回车键'''
    #
    # def enter_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.ENTER)
    #
    # '''全选'''
    #
    # def select_all_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'a')
    #
    # '''复制'''
    #
    # def copy_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'c')
    #
    # '''剪切'''
    #
    # def cut_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'x')
    #
    # '''粘贴'''
    #
    # def paste_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.CONTROL, 'v')
    #
    # '''向下滚动'''
    #
    # def roll_down_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.PAGE_DOWN)
    #
    # '''向上滚动'''
    #
    # def roll_up_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.PAGE_UP)
    #
    # '''到顶部'''
    #
    # def get_top_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.HOME)
    #
    # '''到底部'''
    #
    # def get_bottom_key(self, loc):
    #     self.driver.find_element(*loc).send_keys(Keys.END)


    ###########################截屏##########################################
if __name__ == '__main__':
    pass