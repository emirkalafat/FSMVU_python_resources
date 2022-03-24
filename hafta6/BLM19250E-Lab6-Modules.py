#!/usr/bin/env python
# coding: utf-8

# ## Storing your functions in modules

# ### Example 1 - Distance Example
# 
# - These metrics (Manhattan, Euclidean, Supremum etc.) use to measure the distance between two given points.

# In[1]:


# Import only manhattan and supremum functions from distance.py
from distance import manhattan, supremum

x1 = 1
y1 = 2
x2 = 3
y2 = 5

print(f"Manhattan Distance: {manhattan(x1, x2, y1, y2)}")
print(f"Supremum Distance: {supremum(x1, x2, y1, y2)}")

# Error - Euclidean function is exists but we don't import this function.
print(f"Euclidean Distance: {euclidean(x1, x2, y1, y2)}")


# In[3]:


# Import functions and variables from distance.py
import distance as ds

print(f"Euclidean Distance: {ds.euclidean(x1, x2, y1, y2)}")
print(f"Manhattan Distance: {ds.manhattan(x1, x2, y1, y2)}")
print(f"Supremum Distance: {ds.supremum(x1, x2, y1, y2)}")


# ### Example 2 - Statistics Example
# 
# - Let's create our own statistics functions and call them (mean, stdev, mod, median)

# In[4]:


from mystats import mean, stdev

_list = [1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
print("Mean of List:", mean(_list))
print("Standart Deviation of List:", stdev(_list))


# In[5]:


import mystats

print("Mean of List:", mystats.mean(_list))
print("Standart Deviation of List:", mystats.stdev(_list))
print("Mod of List:", mystats.mod(_list))
print("Median of List:", mystats.median(_list))


# In[ ]:




