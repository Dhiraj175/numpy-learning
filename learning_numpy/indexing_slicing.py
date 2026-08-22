import numpy as np

arr = np.array([12,15,17,9,20])

# Index - Specific element/ location
print(arr[2])

# Slicing -- range/section of array  -- range of position
print(arr[1:4])



## 2D indexing & slicing
arr_2d = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# indexing
print(arr_2d[2,1])   #require 2 coordinates to locate value
print(arr_2d[1])   # give entire row
print(arr_2d[1,:]) # give entire row
print(arr_2d[:,1]) # give entire column
print(arr_2d[1].shape)  # indexing changes shape

# slicing
# arr[row_start:row_stop, column_start:column_stop]
print(arr_2d[:2,1:3])
print(arr_2d[-2:,-2:])  # last 2 * 2 block
print(arr_2d[:2].shape)



## 3D indexing & slicing
arr_3d = np.array([
    [
        [4,7,6,3],
        [12,74,96,89],
        [155,965,746,361]
    ],
    [
        [748,964,746,314],
        [62,42,31,20],
        [9,4,3,5]
    ]
])

print(arr_3d.shape, arr_3d.ndim)
print(arr_3d[1,2,0])   # layer, row, column

print(arr_3d[0 , 1:4, -2:])


# fancy indexing or advanced indexing.
arr = np.array([12,15,17,9,20])

print(arr[[2,1,4]])  # if we want multiple  not continues indexes 
print(arr_2d[[2,1]])  # for 2D array
print(arr_2d[[2,1],[2]])  # with row and column



## Boolean indexing
marks = np.array([46,96,100,74,65,75,34,68,31,15])
passed = marks[marks >= 60]  # marks >= 60 -- This is a Boolean mask.
print(passed)
distinct = marks[(marks >=60) & (marks <= 80)]   # & - element-wise AND. ! - element wise or  ---- not use and & or - normal python for  element-wise NumPy conditions.
print(distinct)



# Slicing often returns a VIEW
arr = np.array([12,15,17,9,20])
part = arr[1:3]
part[0]=700    ## NumPy slicing generally creates a view into the original array rather than copying the underlying data.so changes in part reflect in arr
print(arr) 

part1 = arr[1:3].copy()  # independent 
part1[1] = 900
print(arr)


# arr[1:4]          → usually view
# arr[1:4].copy()   → independent copy





# ============================================================
# Practice 
# ============================================================

a = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120],
    [130,140,150,160]
])

# Write NumPy expressions to extract:
# 1. 70
print(a[1,2])

# 2. Entire second row
print(a[1])


# Entire third column
print(a[:,2])


# [[60,70],[100,110]]
print(a[1:3,1:3])

# Last two rows
print(a[-2:])
# Last two columns
print(a[:, -2:])


# Bottom-right 2 × 2 block
print(a[-2:, -2:])

# First and third rows
print(a[[0,2]])   # fancy indexing 



data = np.array([
    [18, 55, 70],
    [21, 80, 85],
    [17, 45, 60],
    [25, 90, 95],
    [20, 72, 78]
])

# Write NumPy expressions for:
# 1. Extract all ages
print(data[:,0])

# Extract all Math scores
print(data[:,1])

# Extract Math + English as a 2D array
print(data[:, 1:3])

# Select complete rows where Age >= 20
above_20 = data[data[:,0] >= 20]
print(above_20)

# Select complete rows where Math >= 75
print(data[data[:,1]>=75])


# Select complete rows where Age >= 18 AND Math >= 70
print(data[(data[:,0] >= 18) & (data[:,1]>= 70)])


# Extract only English scores for students whose Math >= 75
print(data[data[:,1]>=75][:,2])
print(data[data[:,1]>=75,2])  ## row,column



sales = np.array([
    [120,150,90,180],
    [80,200,140,110],
    [170,160,220,190],
    [60,95,130,85]
])

# Rows = Products (P1–P4)
# Columns = Quarters (Q1–Q4)

# Extract Q2 sales for all products.
print(sales[:,1])

# Extract P3's complete sales history.
print(sales[2])

# Extract the last two quarters for every product.
print(sales[:,-2:])

# Extract the bottom-left 2×2 block.
print(sales[-2:,:2])

# Select products whose Q3 sales are greater than 120.
print(sales[sales[:,2]>120])

# Return only Q4 values for products whose Q2 sales are at least 150.
print(sales[sales[:,1]>=150,3])

# Extract products P1 and P4, but only Q1 and Q4 (expected shape (2,2)).
print(sales[[0,3],[0,3]])   # its wrong it just give me (2,)
print(sales[[0,3]][:,[0,3]])



marks = np.array([
    [45, 78, 91, 66],
    [88, 72, 69, 95],
    [56, 84, 77, 81],
    [92, 65, 89, 73],
    [71, 90, 68, 87]
])
# Students 0, 2, 4 → all subjects
print(marks[[0,2,4]])

# All students → subjects 1 and 3
print(marks[:,[1,3]])

# Students 1 and 3 → subjects 0 and 2, expected shape (2,2)
print(marks[[1,3]][:,[0,2]])

# Complete rows where subject 2 >= 80
print(marks[marks[:,2]>=80])

# Only subject 3 marks where subject 0 >= 70
print(marks[marks[:,0]>=70,3])

# Complete rows where subject 0 >= 70 AND subject 3 >= 80
print(marks[(marks[:,0]>= 70) & (marks[:,3]>=80)])
