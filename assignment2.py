#!/usr/bin/env python
# coding: utf-8

# # Assignment 2

# In[9]:


#InstructionsForPlane

height = int(input('Input altitude :'))
if height == 1000:
    print('The plane is safe for landing :) ')
    print('Plane landed successfully')
elif height < 4500 :
    print('Bring down the plane to 1000 ft ')
elif height > 5000 :
    print('Turn around and try after some time')   
elif height < 1000 :
    print('Land the plane')


# In[ ]:




