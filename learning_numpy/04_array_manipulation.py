import numpy as np

# 1 Reshape -- reshape()
arr = np.array([4,8,6,9,2,37])
print(arr.shape)
new_arr = arr.reshape(2,3)
print(new_arr.shape)

# OLD total elements = NEW dimensions multiplied together

# -1 in reshape
arr = np.arange(12)
print(arr)
new_arr = arr.reshape(4,-1)   # -1 --> NumPy calculates the missing dimension. i.e 3
print(new_arr)
new_arr = arr.reshape(-1,6)
# new_arr = arr.reshape(-1,-1) # invalid insuffient info
print(new_arr)



## 2. Flattening  
# 1. flatten ()  -- "Give an independent 1D copy."
arr = np.array([
    [10,20,30],
    [40,50,60]
])
print(arr.shape,)
flat = arr.flatten()
print(flat.shape)
flat[1] = 175
print(flat)  ## flatten return copy so arr won't change
print(arr)


# 2. ravel()  -- Give a 1D representation; avoid copying if possible
arr = np.array([
    [10,20,30],
    [40,50,60]
])

ravel_arr = arr.ravel()
print(ravel_arr)
ravel_arr[0] = 999
print(ravel_arr)  # ravel() returns a view whenever possible; in some cases it must return a copy.
print(arr)


## Transpose  -- .T or transpose()
# row <-> column
arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr.T)




# Concatenation --> Join existing arrays along an existing axis.
a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.concatenate((a,b)))


# Concatenate 2D arrays — axis=0
# axis=0 → add/join rows  - vertically
# the number of columns must match.
a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(np.concatenate((a,b),axis=0))


# Concatenate 2D arrays — axis=1
# axis=0 → add/join column  -- horizontally
# the number of rows must match.
a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(np.concatenate((a,b),axis=1))


## Stacking
# np.stack() creates a NEW axis
# Join along a NEW axis
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.stack((a,b)))

print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))




## Splitting arrays
# np.split()  -- equal split required
arr = np.arange(12)
print(np.split(arr,6))

# np.array_split()
# unequal split allowed
arr = np.arange(1,14)
print(np.array_split(arr,6))

#Split at specific positions
arr = np.arange(12,32)
print(np.split(arr,[4,9,11]))


# Splitting 2D arrays
arr = np.array([
    [1,2],
    [3,4],
    [5,6],
    [7,8]
])

print(np.split(arr,2,axis = 0))
print(np.split(arr,2,axis = 1))



## Insert 
arr = np.array([4,8,9,3])
arr = np.insert(arr, 2, [99,74,63])
print(arr)


 # 2d array
a = np.array([
    [1,2],
    [3,4],
    [7,9]
])
# a = np.insert(a,0,[76,96],axis=0)
a = np.insert(a,0,[76,96,74],axis=1)
print(a)



# Delete
arr = np.array([4,8,9,3,789,254,87,86])
arr = np.delete(arr,3)  # delete single
print(arr)
arr = np.delete(arr,[1,5])
print(arr)

# delete row  & column
a = np.array([
    [1,2],
    [3,4],
    [7,9]
])
# a_new = np.delete(a,1,axis=0)  # row
a_new = np.delete(a,1,axis=1)  # column
print(a_new)




# ============================================================
# Practice 
# ============================================================

# Practice Level 1 — Reshape
arr = np.arange(1, 13)

# Write expressions for:
# Reshape into (3,4).
print(arr.reshape(3,4))

# Reshape into (4,3).
print(arr.reshape(4,3))

# Reshape into (2,2,3).
print(arr.reshape(2,2,3))

# Reshape into 3 rows using -1.
print(arr.reshape(3,-1))

# Convert it into shape (12,1).
print(arr.reshape(-1,1))

# Convert it into shape (1,12).
print(arr.reshape(1,-1))

# Flatten a (3,4) version using flatten().
print(arr.flatten())

# Flatten it using ravel().
print(arr.ravel())



# Practice Level 2 — Transpose + Combine
a = np.array([
    [1,2,3],
    [4,5,6]
])

b = np.array([
    [7,8,9],
    [10,11,12]
])

# Write expressions to:
# Transpose a.
a = a.T
print(a)

# Check the shape before and after transpose.
print(b.shape)
b = b.T
print(b.shape)

# Combine a and b to produce shape (4,3).
a = a.T
b = b.T
new_ab = np.concatenate((a,b),axis=0)  ## combine in same existing axis 
print(new_ab.shape)

# Combine a and b to produce shape (2,6).
new_ab = np.concatenate((a,b),axis=1)
print(new_ab.shape)

# Explain which axis you used in #3 and why.
# axis = 0 because my current shapes are (2,3) & (2,3) - i want (4,3) that means i want to add 2nd array as row 

# Explain which axis you used in #4 and why.
# axis = 1 because shapes are (2,3) & (2,3) - i want (2,6) that means add columns so axis 1



x = np.array([10,20,30])
y = np.array([40,50,60])

print()
print(np.concatenate((x,y),))
print(np.concatenate((x,y),).shape)  # 6,

print(np.stack((x,y), axis=0))
print(np.stack((x,y), axis=0).shape)    #2,3

print(np.stack((x,y), axis=1))
print(np.stack((x,y), axis=1).shape) #3,2

print(np.vstack((x,y)))
print(np.vstack((x,y)).shape)  #2,3

print(np.hstack((x,y)))
print(np.hstack((x,y)).shape)  # 6,




# Practice Level 3 — Split / Insert / Delete
arr = np.arange(10, 90, 10)


# Write expressions to:
# Split into 4 equal arrays.
print(np.split(arr,4))

# Split at positions 2 and 5.
print(np.split(arr,[2,5]))

# Insert 99 at index 3.
arr = np.insert(arr,3,99)
print(arr)

# Delete the element at index 5.
arr = np.delete(arr,5)
print(arr)

# Delete elements at indices 1 and 6.
arr = np.delete(arr,[1,6])
print(arr)




X = np.array([
    [20, 50, 70],
    [25, 60, 80],
    [30, 75, 90],
    [35, 85, 95]
])
new_feature = np.array([100,200,300,400])

new_feature = new_feature.reshape(-1,1)
print(np.concatenate((X,new_feature),axis=1))