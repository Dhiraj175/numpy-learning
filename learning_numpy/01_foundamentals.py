import numpy as np

## Array vs List
python_list = [8,89,6,7,6,34,5,6]
numpy_array = np.array([7,96,3,796,3274,8])
print(python_list,type(python_list))
print(numpy_array,type(numpy_array))   ## ndarray 

a = [1,4,7]
b = [2,5,8]
print(a+b)   ## list concatination 

c = np.array([1,4,7])
d = np.array([2,5,8])
print(c+d)  ## numpy perform element wise addition 


## 1D array
arr1 = np.array([4,5,6])
# one directional - one index/direction require to locate an element



## 2D array
arr2 = np.array([
    [1,5,9],
    [3,5,7]
])
# 2 dimentional -- require 2 coordinate to locate element 
# Row -- sample ,  Column -- feature
print(arr2[0,2])


## 3D array 
arr3 = np.array([
    [
        [4,5,6],
        [7,8,9]
    ],
    [
        [7,4,6],
        [9,6,3]
    ]
])

# 3D -- require 3 coordinates 
# layer, row, column 
print(arr3[1,0,2])



## List to array
python_list = [8,89,6,7,6,34,5,6]
np_arr = np.array(python_list)



## Arrays can contain different numerical types
numpy_array1 = np.array([7,96,3,796,3274,8])
numpy_array2 = np.array([7.8,96,3.0,796,32,100.02])
print(numpy_array1.dtype)
print(numpy_array2.dtype)

numpy_array3 = numpy_array1 + numpy_array2   ##element wise addition
print(numpy_array3)
print(numpy_array3.dtype)


## change dtype intentionally
arr5 = np.array([4,3,8,9,5])
arr5_float = arr5.astype(float)
print(arr5_float)
print(arr5_float.dtype)



# ============================================================
# EXPERIMENTS
# ============================================================

# 1
temperature = np.array([12,35,42.04,55.92,37])
print(temperature)
print(temperature.dtype)

celsius_fahrenheit = temperature * (9/5)+32
print(celsius_fahrenheit)

#2 student & marks
marks = np.array([
    [32,78,58],
    [99,76,85],
    [78,65,43]
])

print(marks+1)      # scaler operation -- scalar means one value
print(marks.dtype)  #what type of date? -- int64,float64
print(marks.shape)  #(row,column) (4,3)
print(marks.ndim)   # diamention
print(marks.size)   # total element/values - row*column