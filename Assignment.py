#!/usr/bin/env python
# coding: utf-8

# In[16]:


get_ipython().run_line_magic('time', 'l = range(1000000)')
print(l)


# In[11]:


import numpy as np


# In[26]:


# Simple methods
import numpy as np
x = np.array([55, 78, 9, 8, 7])
x.sum()


# x.sum()

# In[40]:


# Max num
print("The Highest Number is",x.max())
print("The index Highest Number is",x.argmax())


# In[42]:


# Min num
print("The smallest Number is",x.min())
print("The index of smallest Number is",x.argmin())


# In[57]:



# Logical "AND" operation of a boolean array
np.any([False, True, True, True])


# In[59]:



# Logical "OR" operation of a boolean array
np.any([False, True, True, True])


# In[65]:


# Setting all the elements of an array to 0
a = np.zeros((121, 10, 150, 0)) #np.zeros convrt every element of arrray to 0
print(a)
print(np.any(a != 0)) # any search for any 1 in array
np.all(a != 0) # all function is used to search from whole array 


# In[66]:


# Setting all the elements of an array to 0
a = np.zeros((100, 100))
np.all(a == 0)


# In[72]:


# conditional function 
a = np.array([51, 2, 25, 2])
b = np.array([52, 2, 3, 2])
c = np.array([6, 4, 27, 5])
((a <= b) & (b <= c)).all() # it will check each element of both condition


# In[76]:


# conditon usion or 
a = np.array([1, 12, 3, 2])
b = np.array([2, 2, 3, 2])
c = np.array([6, 4, 4, 5])
((a <= b) | (b <= c)).all() # if one condition is true it will be true


# In[80]:


# diagnol elements 
arr = np.eye(3) # eye functions makes all diagnol elements 1 and set remaining to 0
print(arr)


# In[79]:


arr1 = np.eye(3,4) # 3 rows 4 column no sequence because rows != column
print("here is rectangle array ")
arr1


# In[82]:


arr1 = np.eye(4,4) # We can mention rows and column. 4 rows 4 column 
print("here is square array ")
arr1


# In[84]:


# diag: This function creates a two dimensional 
#array with all the diagonal elements as the given value
#and rest as 0 (in a square matrix).
arr = np.diag([21,25,43,7]) # thru diag function you can assign custom values to the diagnol elements remainig will be 0
arr


# In[88]:


# get diagnol elements 
np.diag(arr) # make it function and pass array name as value
print("The diagnol elements are")
np.diag(arr)


# In[96]:


# This randomint funciton is used to generate integer values randomly
#number between a given range.
#The syntax is:
#randint(min,max,total_values)
arr = np.random.randint(-10,10,5) # at every execution value will be diffrent
arr


# In[97]:


# This simple rand function generate floating values randomly from 0 to 1
#between 0 to 1
#The syntax is: 
#rand(number_of_values)
arr = np.random.rand(5)
arr


# In[98]:


arr = np.random.rand(2, 3) # generate random float numbers in 2D array format as well
arr


# In[114]:


#This randn function generate random values can be any
#This may return positive or negative numbers as well.
#The syntax is:
#randn(number_of_values)
arr = np.random.randn(3)  # value can be any
arr


# In[124]:


# There would be a starting point and an ending point along
#with the interval value.
arr = np.arange(-25,25,5) # np.arange(starting value , end value , increment_value)
arr


# In[126]:


# it will automatically be incremented by 1
arr = np.arange(-2, 17)
arr


# In[129]:


# sin. Print sine of one angle:
np.sin(np.pi/4)


# In[142]:


# Print sines of an array of angles given in degrees:
np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180. ) # ask the teacher about pi function


# In[139]:


print(np.pi)


# In[143]:


#Method 16: cos.
np.cos(np.array([0, np.pi/2, np.pi]))


# In[146]:


#Method 16: tan
from math import pi
np.tan(np.array([-pi,pi/2,pi])) # logic is not clear


# In[164]:


#Method 17: round.
np.round(16.0955, 3), round(16.0965, 3) # np.round(value, number_decimal_values)


# In[165]:



#Method 18: floor. Return the floor of the input, element-wise.
#The floor of the scalar x is the largest integer i, such that i <= x.
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
np.floor(a)# round to lower value


# In[167]:



#Method 18: floor. Return the floor of the input, element-wise.
#The floor of the scalar x is the largest integer i, such that i <= x.
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
np.ceil(a)# round to upper value


# In[169]:


# the fractional part of the signed number x is discarded.
a = np.array([-1.7, -1.5, -0.2, 0.2, 1.5, 1.7, 2.0])
np.trunc(a) # Truncate the decimal value


# In[170]:


np.prod([]) # PRoduct of empty arrays = 1


# In[186]:


np.prod([[2.,3.,4],[2.,4.,5]]) # 2 dimentional array multiplys 1st element to the next and so on but number of col must be equal


# In[204]:


# cumsum. Return the cumulative sum of the elements along a given axis.
a = np.array([[[1,2,3], [4,5,6],[7,8,9]]])
a


# In[205]:


np.cumsum(a,axis=1)# ADDS 1ST ROW TO THE NEXT


# In[203]:


np.cumsum(a,axis=2)# ADDS 1ST COL TO THE NEXT


# In[209]:


# lcm. Returns the lowest common multiple of |x1| and |x2|
np.lcm(3, 2)


# In[216]:


# gcd. Returns the lowest common divider of |x1| and |x2|
np.gcd(4, 18)


# In[226]:


# transpose. Reverse or permute the axes of an array; returns the modified array
x = np.arange(6).reshape((2, 3)) # can be molded to require shape
x


# In[227]:


np.transpose(x) # five the transpose


# In[228]:


# capitalize. Return a copy of a with only the first character of each element capitalized.
c = np.array(['a1b2','1b2a','b2a1','2a1b'],'S4'); c


# In[230]:


np.char.capitalize(c) # capitalize the 1st letter


# In[233]:


d = np.char.upper(c)


# In[234]:


d


# In[235]:


e = np.char.lower(d)


# In[236]:


e


# In[245]:


c = np.array(['aAaAaA', '  aA  ', 'abBABba'])
d = np.char.count(c,'BA')
d


# In[254]:


# linspace. This function returns values 
#between a given range and with a same gap between
#consecutive elements.
np.linspace(1,15,30)


# In[262]:


matrix = np.random.randint(0,8,9).reshape(3,3)
matrix


# In[263]:


np.min(matrix, axis=1) #finds row wise min


# In[264]:


np.max(matrix, axis=0) #finds col wise max


# In[265]:


np.sum(matrix, axis=1) #finds row wise sum


# In[268]:


np.sum(matrix, axis=0) #finds col wise sum


# In[269]:


np.cumsum(matrix) #finds cumulative sum


# In[278]:


# shuffle. shuffle the array elements.
np.random.seed(122) # logic not clear
arr = np.random.randint(1,21,10)
arr


# In[279]:


np.random.shuffle(arr)
arr


# In[280]:


# unique. displays unique number of the array.
np.unique(arr)


# In[299]:


# argsort. prints the sorted index value wise ascending
one = np.array([5,4,2,6])
one


# In[303]:


ASSENDING = one.argsort() #PRINT THE ORDER OF VALUES LOWER TO HIGER


# In[304]:


ASSENDING


# In[319]:


x = [[1,2,3],[4,0,6],[7,1,0]]
arr = np.array(x)
arr


# In[320]:


np.where(arr >= 4) # logic not clear


# In[321]:


# count_nonzero
np.count_nonzero(arr)


# In[322]:


# sort. It is used to sort an array
a = np.array([[1,4], [3,1]])
a


# In[324]:


a.sort(axis=1) # sort inside row
a


# In[327]:


a.sort(axis=0)
a


# In[338]:


# variance. var.
a = np.array([[1, 2], [4, 0]])
np.var(a)# logic not clear


# In[348]:


# Split. Split an array into 
#multiple sub-arrays as views into ary.
x = np.arange(16.0)
np.split(x, 4)


# In[353]:


x = np.arange(10.0)
np.split(x, [3,5,6,15])


# In[357]:


# delete. Return a new array with sub-arrays along an axis deleted. For a one dimensional array, this returns those
#entries not returned by arr[obj].
arr = np.array([[1,2,3,4], [5,6,7,8],[9,10,11,12]])
arr


# In[364]:


np.delete(arr, 0, 0)


# In[ ]:




