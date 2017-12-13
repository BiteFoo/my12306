# -*- coding:UTF-8 -*-
'''
author:Loopher

date:2017-12-13

description: 
登陆和选择票信息
'''
import sys

import time
from selenium import webdriver

login_url = 'https://kyfw.12306.cn/otn/login/init'

book_ticket_url = ''

class Ticketor(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self.brower = webdriver.Chrome('chromedriver')
        pass

    def __init_data(self):
        '''
        初始化数据
        :return:
        '''
        if self.args is not None:
            self.username = self.args[0]
            self.password = self.arg[1]

    def __waite_click_register_code_by_user(self):
        '''
        等待输入验证码
        只等待
        :return:

        '''
        count = 0
        while True:
            count += 1
            if count > 10:
                print('[ERRO]: total %d times ' % count)
                return -1
            curr_url = self.brower.current_url
            if curr_url != login_url:
                if curr_url[:-1] != login_url:
                    print('[DEBUG]: login finished !! ')
                    break
            else:
                time.sleep(5)  # 每次等待5秒
                print('[DEBUG]:  %d times' % count)
                print('[DEBUG]:waiting for user to check regCode ')
        return 0

    def __login(self):
        '''
        登陆
        :return: 0 ：success  -1 failure
        '''
        try:
            self.brower.implicitly_wait(30)
            self.brower.get(login_url)
            user_input = self.brower.find_element_by_id('username')
            user_input.clear()
            if self.username is None:
                print('[Error]: %s must not be NoneType' % ('username'))
                return -1
            user_input.send_keys(self.username)
            password_input = self.brower.find_element_by_id('password')
            password_input.clear()
            if self.password is None:
                print('[Error]: %s  must not be NoneType' % ('password'))
                return -1
            password_input.send_keys(self.password)
            return  self.__waite_click_register_code_by_user()
        except:
            print('[Exception]: login error ')
            sys.exit(1)

    def __choose_time_start(self):
        '''
        选择出发时间日期
        :return:
        '''
        pass

    def __choose_passener(self):
        '''
        选择乘车人
        :return:
        '''
        pass

    def __run_scan_tickets(self):
        '''
        查找票信息
        :return:
        '''
        pass

    def start_run(self):
        '''
        启动程序执行
        :return:
        '''
        if self.__login() == 0:
            self.__run_scan_tickets()
        else:
            print('[Error]: 登陆失败 ！！！ ')


def main():
    ticketor = Ticketor()
    ticketor.start_run()

    pass


if __name__ == '__main__':
    print("errir")
    main()
