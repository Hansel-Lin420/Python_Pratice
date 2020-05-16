# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:38:48 2020

@author: User
"""
for i in range(1,100):
    if 168 % i == 0:
        j = 168 / i;
        if  i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0 :
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)