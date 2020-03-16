#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Guan Xin
#2020-02-07


import os
import sys
import time
import GlobalVariable
import shutil
import logging
sys.path.append(os.path.dirname(os.path.abspath(__file__))+r'\venv\lib\site-packages\\')
import pymysql
import datetime
current_date = time.strftime("%Y-%m-%d", time.localtime())  # 获取日期
current_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())  # 获取当前时间，用于备份和删除日志文件
current_stamp = round(time.time())  # 获取当前时间戳然后四舍五入取整
current_path = os.path.abspath(__file__)  # 获取当前文件绝对路径


'''用例开始前备份前7天的日志文件'''

def backup_log():  # 备份并清空logs目录
    backup_logs = 'backup_logs'
    log_path = GlobalVariable.Path['Immediate_path']
    backup_path = log_path  + backup_logs + r'\\'  # 日志备份路径
    if os.path.exists(backup_path):
        shutil.rmtree(backup_path)
    dir_list = os.listdir(log_path)  # 列出所有日志文件
    print(dir_list)
    for i in dir_list:
        i_path = os.path.join(log_path, i)
        if os.path.isfile(i_path):
            os.remove(i_path)
        else:
            shutil.copytree(i_path, os.path.join(backup_path, i))
            shutil.rmtree(i_path)


'''没有文件则创建文件'''


def new_file(path):
    if os.path.exists(path):
        pass
    else:
        with open(path, 'w', encoding='utf-8') as f:
            pass


'''修改文件名称'''


def rename_caselog(lst):  # 修改日志文件名称为文件夹名称+.log
    new_log_path = GlobalVariable.Path["Immediate_path"] + lst[1] + '_' + lst[0]+'_'+lst[3]+'_'+lst[4]
    src = new_log_path + '\\' + GlobalVariable.case_excute_res[2]
    print(src)
    dst = new_log_path + '\\' + lst[1] + '_' + lst[0]+'_'+lst[3]+'_'+lst[4] + '.log'
    print(dst)
    if os.path.exists(src):
        try:
            os.rename(src, dst)
        except BaseException as b:
            case_log()[0].error("修改文件出错"+str(b)+'\n')


'''删除文件'''


def del_file(file_path):
    fun_name = sys._getframe().f_code.co_name
    try:
        os.remove(file_path)
    except BaseException as b:
        get_error(current_path, fun_name, str(b))
        raise b


'''写入error日志文件'''


def get_error(*res):
    try:
        if len(res) != 0:
            with open(GlobalVariable.Path["error_log"], 'a') as f:
                for i in res:
                    if i != res[-1]:
                        f.write(i+'_')
                    else:
                        f.write(i+'\n')
    except BaseException as b:
        raise b


'''保存日志,TODO并复制截图到日志文件夹'''


def save_log(lst):
    fun_name = sys._getframe().f_code.co_name
    try:
        case_floder = lst[1] + '_' + lst[0]+'_'+lst[3]+'_'+lst[4]  #用例执行完成的文件夹名称
        dst = GlobalVariable.Path["Immediate_path"] + case_floder
        if os.path.exists(dst):
            shutil.rmtree(dst)
        os.mkdir(dst)
        src = GlobalVariable.Path["Immediate_path"]+GlobalVariable.case_excute_res[2]
        os.system('copy %s %s' % (src, dst))
    except BaseException as b:
        get_error(current_path, fun_name, str(b))
        raise b


'''日志模块'''


def case_log(type):
    fun_name = sys._getframe().f_code.co_name
    global th
    global logger
    try:
        logname = current_date + r'-%slogs.log' % (type)
        print(logname)
        if logname not in GlobalVariable.case_excute_res:
            GlobalVariable.case_excute_res.append(logname)
        log_path = GlobalVariable.Path["Immediate_path"]+r'\\'+logname
        logger = logging.getLogger(logname)
        logger.setLevel(logging.INFO)  # 设置日志级别
        fmt = '%(asctime)s_%(name)s_%(pathname)s_%(lineno)d>>>%(levelname)s:%(message)s'
        log_style = logging.Formatter(fmt)  # 设置日志格式
        if not logger.handlers:
            sh = logging.StreamHandler()  # 往屏幕上输出
            sh.setFormatter(log_style)
            th = logging.FileHandler(log_path, mode='w')
            th.setFormatter(log_style)  # 设置文件里写入的格式
            logger.addHandler(sh)  # 把对象加到logger里
            logger.addHandler(th)
    except BaseException as b:
        get_error(current_path, fun_name, str(b))
        raise b
    finally:
        return logger, th


class OpreationMysql:

    # self.logger.info(self.Conf_path)
    conf = GlobalVariable.Mysql
    h = conf["host"]
    u = conf["username"]
    p = conf["password"]
    port = int(conf["port"])
    db = conf["datebase"]

    def __init__(self):
        self.logger = case_log('mysql')[0]
        self.connect = self.connect_db()
        self.class_name = self.__class__.__name__
        if (self.connect):
            self.cursor = self.connect.cursor()
    def connect_db(self):
        fun_name = sys._getframe().f_code.co_name
        try:
            connect_info = self.h + ":" + str(self.port) + "/" + self.db + ",用户名：" + self.u + "，密码:" + self.p
            self.logger.info("开始连接数据库：%s" % (connect_info))
            connect = pymysql.Connect(host=self.h, user=self.u, passwd=self.p, port=self.port, db=self.db)
            self.logger.info("连接数据库成功")
        except BaseException as e:
            get_error(current_path, self.class_name, fun_name, str(e))
            connect = False
            raise e
        finally:
            return connect
    def close_db(self):
        fun_name = sys._getframe().f_code.co_name
        try:
            self.cursor.close()
            self.connect.close()
            self.logger.info("数据库关闭成功")
        except Exception as e:
            get_error(current_path, self.class_name, fun_name, str(e))
            raise e

    def select(self, sql):
        fun_name = sys._getframe().f_code.co_name
        res = ''
        if (self.connect):
            try:
                self.cursor.execute(sql)
                res = self.cursor.fetchall()
                self.logger.info(res)
            except Exception as e:
                get_error(current_path, self.class_name, fun_name, str(e))
                res = False
                raise e
        self.close_db()
        return res


if __name__ == '__main__':
    OpreationMysql().connect_db()
    sql = "select `name`,`serial`,`category`,`dept_name`,`enabled` FROM `nw_tool` where " \
          "dept_name='750kV兰州东变电站' and category like'%验电器' and enabled=0;"
    tool = OpreationMysql().select( sql )
    print(tool)
    OpreationMysql().close_db()