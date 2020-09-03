#!/usr/bin/env python
# coding: utf-8

# Assignment 3 : Print prime numbers between 1-200 using For loop and Range function 

# In[ ]:
for i in range(0,200) :
    for j in range(2,i):
        if i / j == 0 :
            break
        else :
            print(i)

