'''
Numpy Library
'''
import numpy as np
import random

my_list =[[1,2,3],[4,5,6]]
arr =np.array(my_list)
#print(arr)
new_list1 =np.arange(0,100,2) # creates an 1d array from 0 to 99 only even integers 0- start, 100- end, 2= step
new_list2 =np.ones((5,5)) #it creates array with all cells as 0 5X5 array
new_list3 =np.zeros((4,4))#it creates array with all cells as 1 4x4 array
new_list4 =np.eye((5))# identity matrix with 5X5
#print(new_list4)

ran = np.random.rand(10) #[0.52160888 0.74398001 0.34912046 0.17035084 0.81730404 0.78558793,0.84486162 0.86619933 0.77250248 0.12598374]
rand_int =np.random.randint(0,2000,5)# [ 228  592 1106  423  730]
#print(rand_int)

new_shape =new_list1.reshape(5,10)
'''
print(new_shape)
[[ 0  2  4  6  8 10 12 14 16 18]
 [20 22 24 26 28 30 32 34 36 38]
 [40 42 44 46 48 50 52 54 56 58]
 [60 62 64 66 68 70 72 74 76 78]
 [80 82 84 86 88 90 92 94 96 98]]'''
maxi =new_shape.max() #98
maxi_index =new_shape.argmax()#49
mini =new_shape.min()#0
mini_index =new_shape.argmin()#0

print(new_shape.shape) #(5,10)
print(new_shape.dtype) #int64
dt = np.dtype(np.int32)
print(dt)

# Numpy operations
#Array with Array
#Array with Scalars
#Universal Array Functions
arr =np.arange(1,11)
print(arr)#[1  2  3  4  5  6  7  8  9 10]
arr1 =arr+arr
print(arr1)#[ 2  4  6  8 10 12 14 16 18 20]
arr2 =arr-arr
print(arr2)#[0 0 0 0 0 0 0 0 0 0]
arr3 =arr*arr
print(arr3)#[ 1   4   9  16  25  36  49  64  81 100]
arr4 =arr/arr
print(arr4)#[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
arr5 =arr3+1000
print(arr5)#[1001 1004 1009 1016 1025 1036 1049 1064 1081 1100]
arr6 = np.exp(arr3)
print(arr6)
'''
for more functions in numpy  checkout this https://numpy.org/doc/stable/reference/ufuncs.html
'''
spa =np.linspace(0,1,20)
print(spa)
new1 = np.arange(1,26).reshape(5,5)
new2 =new1[2:,1:]
print(new2)
new3 =new2.sum()
print(new3)
new4 =new2.sum(axis=0)
print(new4)