#!/usr/bin/env python
# coding: utf-8

# # DAY10 test

# In[1]:


a=int(input("enter your age: "))
if a>60:
    print("welcome to the seniors club")
elif 40<a<60:
    print("yet to be a senior citezen")
else a<40:
    print("you are still young")
print(a)


# In[ ]:





# In[3]:


# Q3
a=int(input("enter your first number : "))
b=int(input("enter your second number : "))
c=a*b
print("product of your two numbers is: ",c)


# In[ ]:


a=["apple","banana","leechi","mango"]


# In[ ]:


a=[55,9,2,9,53,96,87,3]
b=[7,6,52,79,145,6,565]
max(a,b)


# In[ ]:


a=[55,9,2,9,53,96,87,3]
a.sort(reverse=True)
print(a)


# In[30]:


# Q11
a= "football","badminton","tennis"
f,b,t=a


# In[31]:


t


# In[6]:


f


# In[7]:


b


# In[14]:


# Q5
a=[8,87,987,741,963,123,789,5]
c=sum(a)
print(c)


# In[17]:


# Q13
a=[9,"rakno",69,"onkar",741] # appends anything in the end, and takes only one argument
a.append(89)
print(a)


# In[20]:


a.insert(2,"rocks") # insert accepts 2 arguments and make changes to specified index number
print(a)


# In[21]:


a.extend("ram") #seperates everything in the srtring and prints in the end
print(a)


# In[29]:


# Q10
a=["name","age","place"]
b=["onkar","21","pune"]
dict(a)


# In[38]:


#Q12
a=int(input("enter your first num: "))
b=int(input("enter your second num: "))
if a*b<=1000:
    print("product is : ",a*b)
else:
    print("the sum is : ",a+b)


# In[45]:


import numpy as np
a=np.array([[9,52,63,78],[4,698,1,5]])
a.shape


# In[46]:


a.ndim


# In[ ]:




