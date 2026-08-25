import numpy as np

## broadcasting Rule 
# 1. Two dimensions are compatible when:
    # 1. They are equal or 
    # 2. One of them is 1
    
# 2. Compare shapes from RIGHT → LEFT
    # Suppose: A = (4,3)  & B = (3,)
    # then A -> 4,3
    #       B ->  ,3    ---- B has no dimension corresponding to the 4, so NumPy treats the missing leading dimension as 1
    
    ## so now 3 vs 3 - equal 
    ## 4 vs 1 - equal
    
    
    
## Row vector vs Column vector
# Row-style shape -- (1,3)  ---> Broadcasts naturally across rows
# Column style shape -- (3,1)  - Broadcasts naturally across column


## np.newaxis
a = np.array([10,20,30])
print(a.shape)
print(a[:,np.newaxis])    # It inserts a dimension of size 1.  column orientation
print(a[:,np.newaxis].shape)
print(a[np.newaxis,:])
print(a[np.newaxis,:].shape)   # column orientation
print(a[:,None])   # do the same thing



## Practice 1

A = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

B = np.array([1,10,100])

# Without running first:
# 1. Predict A + B.
# a shape - (3,3), B shape - (3,)
#output (3,3)
print(A+B)


# 2. What is A.shape?
# (3,3)


# 3. What is B.shape?
# (3,)


# 4. Explain why broadcasting works.
# a shape is 3,3 & b is 3,
# broadcasting check from rightmost that is 3 vs 3 - same & 3 vs 1 - compatible because one dimension is 1 


# 5. Which values are applied to column 0, column 1 and column 2?
# C0 - 1, C1 - 10 & C2 - 100




## Practice 2

A = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

B = np.array([100,200,300])
# Goal 
# Row 0 → +100
# Row 1 → +200
# Row 2 → +300

print(A + B.reshape(-1,1))



## Practice 3
a = np.array([10,20,30])
b = np.array([1,2,3,4])

# Output: 
# [[11,12,13,14],
#  [21,22,23,24],
#  [31,32,33,34]]

print(a.reshape(-1,1)+b)
print(a[:,np.newaxis]+b)
print(a[:,None]+b)




## practice 4
X = np.array([
    [10,100,1000],
    [20,200,2000],
    [30,300,3000],
    [40,400,4000]
])
mean = X.mean(axis=0)
std = X.std(axis=0)

print(mean, mean.shape)
print(mean-X)



## Practice
data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

a = data[:, np.newaxis, :]
b = data[np.newaxis, :, :]

# 1.  data.shape = ?
# (4,3)

# 2. a.shape = ?
# 4,1,3

# 3. b.shape = ?
# 1,4,3


# 4.  a - b resulting shape = ?
# 4,4,3

print(a.shape)
print(b.shape)