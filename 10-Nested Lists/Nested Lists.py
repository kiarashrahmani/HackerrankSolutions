# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 22:19:37 2023

@author: Kiarash Rahmani
"""
Finallist = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    MyList = []
    MyList.append(name)
    MyList.append(score)
    Finallist.append(MyList)
    MyList = []
    
    

print(MyList)
print(Finallist)