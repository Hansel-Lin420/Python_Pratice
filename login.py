# -*- coding: utf-8 -*-
"""
Created on Sun May 10 23:33:59 2020

@author: User
"""


a = 0
while a < 3:
    name = input("請輸入用戶名： ")
    password = input("請輸入密碼: ")
    a += 1
    if (name == 'wxd' and password == '123456'):
            print("登陸成功")
            exit()
    else:
        print("輸入錯誤，請重新輸入")
print("輸入錯誤三次，退出")