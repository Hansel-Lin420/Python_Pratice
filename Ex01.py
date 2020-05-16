# -*- coding: utf-8 -*-
"""
Created on Mon May 11 12:51:00 2020

@author: User
"""


for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i!=j and j!=k and k!=i):
                print(i,j,k)