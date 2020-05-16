# -*- coding: utf-8 -*-
"""
Created on Sun May 10 22:43:17 2020

@author: User
"""

print("奇數:",end='')
for i in range(1,101):
    if(i%2!=0):
        print(i,end=',')
print()
print("偶數:",end='')
for i in range(1,101):
    if(i%2==0):
        print(i,end=',')