#!/usr/bin/env python
# coding: utf-8

# # #Loops

# # For Loop

# In[4]:


l=[1,28,13,17,18]       # Adding 5 in each element in list using for loop

l2=[]

for i in l:
     l2.append(i+5)


# In[5]:


l2


# In[6]:


l=[]


# In[7]:


for i in range(1,11):                     # in python range is taken as one number less
    l.append(i+5)


# In[8]:


l


# In[2]:


l2=["python","java","php"]             # Doing list in uppercase

l=[]

for i in l2:
    l.append(i.upper())


# In[3]:


l


# In[33]:


l=["python","java","php","r"]        #extract 1st character in the list

l2=[]

l3=[]

for i in l:
    l2.append(i[0].upper())
    


# In[34]:


l2


# In[56]:


l=["abhir_sen","alekhya_reddy"]       # Extract first & last names in separate list

l2=[]

l3=[]

for i in l:
    first,last=i.split("_")
    l2.append(first)
    l3.append(last)


# In[51]:


l2


# In[57]:


l3


# # IF

# In[61]:


x=10

if x==10:
    
   x=17

x
    


# In[62]:


x=14

if x>=17:
   x=10
 
else:
    x=20    


# In[63]:


x


# # if,elif,else

# In[64]:


x=17                                 # It execute only first condition of true if their are 2 true conditions

if x>=19:
    x=18
    
    
elif x>15:
    x=19
    
else:s
    x=12
    


# In[65]:


x


# In[ ]:




