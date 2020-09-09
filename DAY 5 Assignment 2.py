#!/usr/bin/env python
# coding: utf-8

# # DAY 5 Assignment 2

# In[2]:


def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
        else :
            return True
filterlst = filter(isPrime, range(2500))
print('print number btw 1-2500 :', list(filterlst)) 


# In[ ]:




