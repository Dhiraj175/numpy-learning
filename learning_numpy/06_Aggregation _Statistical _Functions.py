import numpy as np
arr = np.array([414,89,-3,79,21,1,0])

# Sum ()
print(arr.sum())
print(np.sum(arr))

# mean = average ()
print(arr.mean())
print(np.mean(arr))

# min() & max()
print(np.min(arr))
print(np.max(arr))


# argmin() & argmax() -- give index
print(np.argmin(arr))
print(np.argmax(arr))



## Aggrigation with 2D array
data = np.array([
    [14,25,36,45],
    [78,95,26,47],
    [94,96,32,46]
])
print(np.sum(data))   ## add all values
print(np.sum(data,axis=0))   # gives one result per column.
print(np.sum(data,axis=1))   # gives one result per row
print(np.argmax(data,axis=0))




## Standard deviation  -- How spread out are values around their mean?

## Variance — var()
# variance = standard deviation²


## median ()


## np.ptp() — range ---- peak to peak
# max - min 
print(np.ptp(data,axis=0))


## np.cumsum() - cummulative sum ---- running total
print(np.cumsum(data,axis=1))


## np.cumprod() 
print(np.cumprod(data,axis=1))


## keepdims=True
print(np.sum(data,axis=1,keepdims=True).shape)



# =======================================================================
# Practice
# =======================================================================

## Practice 1 — Axis
A = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
    [100,110,120]
])

print(A.sum(axis=0))
# shape - 3, --- sum of each feature

print(A.sum(axis=1))
# shape - 4, --- sum of each sample(row)

print(A.mean(axis=0))

print(A.max(axis=1))



## Practice 2 
marks = np.array([
    [50,80,70],
    [90,60,85],
    [75,95,65],
    [88,72,92]
])
# Write expressions to find:
# Highest mark overall.
print(np.max(marks))

# Index of highest mark overall.
print(np.argmax(marks))

# Highest mark for each student.
print(np.max(marks,axis=1))

# Best subject index for each student.
print(np.argmax(marks,axis=1))

# Highest mark for each subject.
print(np.max(marks,axis=0))

# Student index who scored highest in each subject.
print(np.argmax(marks,axis=0))



## Practice 3 — ML-style feature statistics
X = np.array([
    [10,100,1000],
    [20,200,2000],
    [30,300,3000],
    [40,400,4000]
])
# Write expressions for:
# Feature-wise mean.   --- shape 3,
print(np.mean(X,axis=0))

# Feature-wise standard deviation. --- shape 3,
print(np.std(X,axis=0))

# Feature-wise minimum.   --- shape 3,
print(np.min(X,axis=0))

# Feature-wise maximum.   --- shape 3,
print(np.max(X,axis=0))


# Sample-wise mean.   --- shape 4,
print(np.mean(X,axis=1))

# Standardize every feature using: (X - mean) / std   ----- shape 4,3
print((X-np.mean(X,axis=0))/np.std(X,axis=0))



## Build a Distance Matrix
data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

a = data[:,np.newaxis,:]  # 4,1,3
b = data[np.newaxis, :, :] # 1,4,3
diff = a - b   # 4,4,3

squared = diff **2
summed = np.sum(squared,axis=2)
distance = np.sqrt(summed)
print(distance)