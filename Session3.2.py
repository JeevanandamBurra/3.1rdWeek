
# coding: utf-8

# ## 1. Write a function to compute 5/0 and use try/except to catch the exceptions.

# In[3]:


def execp():
    return 5/0

try:
    execp()
except ZeroDivisionError:
    print ("division by zero!")

finally:
    print ('In finally block to Clean.')


# ## 2.  ​Implement a Python program to generate all sentences where subject is in ["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in ["Baseball","cricket"]. 
#  
# Hint: Subject,Verb and Object should be declared in the program as shown below. 
#  
# subjects=["Americans ","Indians"] verbs=["play","watch"] objects=["Baseball","Cricket"] 
#  

# In[12]:


# Option 1
subject=["Americans", "Indians"]
verb=["Play", "watch"]
obj=["Baseball","cricket"]

# Use list comprehension instead of looping
sentence_list = [(sub+" "+ vb + " " + ob+'.') for sub in subject for vb in verb for ob in obj]
for sentence in sentence_list:
    print (sentence)


# In[13]:


# Option 2
subject=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

# Using nested looping to produce the expected output
for i in subject:
    for j in verbs:
        for k in objects:
            print(i+" "+j+" "+k+".")

