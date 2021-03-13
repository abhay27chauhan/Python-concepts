# NumPy is a general-purpose array-processing package. It provides a high-performance multidimensional array object, and tools for working with these arrays. It is the fundamental package for scientific computing with Python

import numpy as np

my_lst = [1, 2, 3, 4, 5]

arr = np.array(my_lst) # 1d array
print(arr)
print(type(arr))
print(arr.shape)  # tells no. of rows and cols of an array
print(arr[3]) # accessing element in 1d
arr[3:] = 100 # make all the elements from index 3 to end equals to 100
print(arr[arr<3]) # prints value which are less than 3


my_lst1 = [1, 2, 3, 4, 5]
my_lst2 = [2, 3, 4, 5, 6]
my_lst3 = [9, 7, 6, 8, 9]

arr1 = np.array([my_lst1, my_lst2, my_lst3]) # 2d array
print(arr1)
print(arr1.shape) # tells rows and cols of an array

##### Print ways ###
print(arr1[:,:]) # another way of printing the whole array
print(arr1[1:,1:]) # print the array from row =1 and col = 1 to end
print(arr1[0:3, 1:4]) # (0:3) -> print from index 0 to 2 | (1:4) -> index 1 to 3
###########


# create array and reshape
arr3 = np.arange(0, 10).reshape(5, 2)
print(arr3)
arr4 = np.arange(0, 10).reshape(5, 2)
print(arr4)

print(arr3*arr4) # multiply 2 arrays

arr5 = np.ones(5) # print all five as 1.
print(arr5)
arr5 = np.ones((2, 5)) # print all as 1. in 2x5 matrix
print(arr5)
arr5 = np.ones((2, 5), dtype=int) # print as 1
print(arr5)


## random distribution
arr5 = np.random.rand(3, 3)
print(arr5)

arr5 = np.random.randint(0, 100, 8).reshape(4, 2) 
print(arr5)

# np.random.random_sample() is one of the function for doing random sampling in numpy. It returns an array of specified shape and fills it with random floats in the half-open interval [0.0, 1.0).
arr5 = np.random.random_sample((1, 5)) # 1, 5 ->  row = 1, col = 5
print(arr5)

