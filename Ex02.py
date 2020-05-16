# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:54:11 2020

@author: User
"""


i = int(input('當月利潤:'))
money = [1000000,600000,400000,200000,100000,0]
bonus = [0.01,0.015,0.03,0.05,0.075,0.1]
prize = 0
for j in range(6):
    if i>money[j]:
        prize+=(i-money[j])*bonus[j]
        i=money[j]
print ("當月獎金為"+str(prize))