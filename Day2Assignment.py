#!/usr/bin/env python
# coding: utf-8

# #  Arithmetic Operations
# 
# 2 + 2 # Addition 

# In[ ]:


# 10 - 4  # Subtraction 


# In[3]:


10 / 5 # Division 


# In[4]:


10 % 3 # ModuloDivision


# In[5]:


10 / 3 # flaotValue


# 

# In[6]:


20 // 6 # Floor division 


# In[7]:


# Boolean & Comparison

print( 7 > 5 )
True
print( 10 < 10 )
False


# In[ ]:





# # Lists : uses big bracket 

# In[10]:


myList = ["suraj", "thakur",21,"nepal"]
print(myList)


# In[12]:


print(myList[0])


# In[14]:


myList.index(21)  #finding index in a list


# # listOperations
# 

# In[20]:


myList = ["suraj", "thakur",21,"nepal"]
print("suraj" in myList)


# In[21]:


print(myList.append("greatwork"))
print(myList)


# In[26]:


print(myList.pop(3))  # delete function


# In[27]:


print(len(myList))  #len function


# # Dictionaries : uses curly bracket

# In[28]:


newDict = {"CPU":1, "RAM":2, "Graphics Card":3, "Mouse":5, "Keyboard":3}


# # Dictionaries functions
# 
# 
# print(newDict["CPU"])

# In[32]:


print(newDict["Mouse"])


# In[33]:


newDict["Desktop"] = 2


# In[34]:


newDict


# In[35]:


print("RAM" in newDict)


# In[36]:


print(newDict.get("Mouse"))


# # Tuple (Immutable) : uses  small bracket

# In[37]:


newTuple = ("CPU", "GPU", "HDD", "SSD", "Procesor")


# In[38]:


print(newTuple[2])


# In[39]:


print(newTuple[4])


# In[41]:


newTuple[0]


# In[43]:


newTuple[3]


# In[ ]:





# In[ ]:




