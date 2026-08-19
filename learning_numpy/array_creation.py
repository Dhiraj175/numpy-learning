import numpy as np

# ============================================================
# Learning
# ============================================================



## 1. np.zeros()
# 1D array
arr_zero = np.zeros((5))  #Creates an array containing zeros.
print(arr_zero)   # default dtype is float64

# 2D array
arr_zero1 = np.zeros((3,4),dtype=int)   # float64 to int64
print(arr_zero1)

# 3D array
arr_zero3 = np.zeros((2,3,4))  # layer,row,column


## np.ones()
arr_ones = np.ones((4,6))
print(arr_ones)
print(arr_ones.dtype)
print(arr_ones.ndim)
print(arr_ones.shape)
print(arr_ones.size)

arr = np.ones((3,5),dtype=int) * 10  #scaler multiplication
print(arr)


## np.full()
# np.full(shape, fill_value)
arr_full = np.full((4,3),17)
print(arr_full)
print(arr_full.dtype)  # defualt dtype is int64

arr_full1 = np.full(3,18)  # 3- shape, 18- fill value



## np.arange()
#syntax: (start,stop,step)
# control steps
arr = np.arange(5,25,5)
print(arr)


## np.linspace() 
# control values (start,stop,values)
arr_arange = np.arange(0,11,2)   # Give values from 0 to 10 with a step of 2.

arr_linspace = np.linspace(0,10,5)  # Give 5 equally spaced values between 0 and 10.
print(arr_linspace)



## np.eye() — Identity Matrix
I = np.eye(4,dtype=int)
print(I)


## np.empty()
arr_empty = np.empty(4)  # Allocate memory for the array without initializing its entries to a known value.
print(arr_empty)


## zeros_like(), ones_like(), full_like()
# *_like() generally inherits the reference array's dtype.
x = np.array([
    [4,8,6],
    [7,3,1]
])

zero_like_mask = np.zeros_like(x)
print(zero_like_mask)

one_like_mask = np.ones_like(x)
print(one_like_mask)

full_like_mask = np.full_like(x,5.7)
print(full_like_mask)
print(full_like_mask.dtype)  # x dtype is int64 so full_like_mask dtype also int64



# ============================================================
# Experiment
# ============================================================

# Challenge 1
# Create a (4, 5) integer array containing only zeros.
a = np.zeros((4,5))

# Challenge 2
# Create a (3, 4) array where every element is 25.
b = np.full((3,4),25)

# Challenge 3
# Generate: 10 20 30 40 50 60 70 80 90 100
c = np.arange(10,101,10) 


# Challenge 4
# Generate 21 equally spaced values from 0 to 1.
d = np.linspace(0,1,21)
print(d)


# Challenge 5
# Create a 5 × 5 identity matrix.
e = np.eye(5)


# Challenge 6
# 1000 training samples
# 20 features 
# create  placeholder feature matrix filled with zeros.
f = np.zeros((1000,20))
# placeholder = temporary/preallocated structure