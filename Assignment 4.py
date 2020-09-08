#!/usr/bin/env python
# coding: utf-8

# # Assignment 4 : Print armstrong number between the range of given numbers.


lower = 1042000
upper = 702648265
for i in range(lower, upper):
    num = i 
    order = len(str(num))
    temp = i 
    sum = 0
    while temp > 0  :
        digit = temp % 10 
        sum += digit ** order
        temp //= 10
    if num ==  sum :
        print("The first armstrong number between the given range is :" , num)
        break 
