import numpy as np

## Element-wise multiplication  & Dot product
a = np.array([1,2,3])
b = np.array([4,5,6])
print(a*b)
print(np.dot(a,b))   # dot product -- summed 4 + 10 + 18 
print(a@b)


rng = np.random.default_rng()

## Matrix multiplication
a = rng.integers(1,20,(2,3))
b = rng.integers(1,30,(3,2))
print(a@b)



## Matrix diagonal 
A = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
print(np.diag(A))


##  Create a diagonal matrix
a= np.eye(4,dtype=int)  # identity matrix
print(a)

b = np.diag([10,20,30,40])
print(b)


## Trace -- Trace is the sum of the main diagonal.
print(np.trace(A))



## Determinant -- for square matrix  --- det = ad - bc
print(np.linalg.det(A))


## Matrix inverse
A_inv = np.linalg.inv(A)
print(A@A_inv)



## Norm -- A norm measures vector magnitude/length.
print(np.linalg.norm(A))





# =======================================================
# Practice
# =======================================================

# Practice 1 — Element-wise vs Dot
a = np.array([2,3,4])
b = np.array([5,6,7])
print(a*b)  # element wise mul -- shape 3,
print((a*b).shape)

print(a@b)  # dot mul  --


## Practice 2 — Matrix multiplication
A = np.array([
    [1,2,3],
    [4,5,6]
])

B = np.array([
    [7,8],
    [9,10],
    [11,12]
])
# A.shape = 2,3
# B.shape = 3,2

# Can A @ B work --- yes 
# inner diamentions should match for matrix multiplication here 3 match 3 so work

# Result shape = 2,2
print(A@B)



## Practice 3 — ML prediction
X = np.array([
    [2,5,3],
    [1,4,2],
    [7,1,6],
    [3,8,2]
])

w = np.array([
    [0.5],
    [2.0],
    [-1.0]
])
# X.shape = 4,3
# w.shape = 3,1
# prediction.shape = 4,1
predication = X@w
print(predication)
print(predication.shape)



## Practice 5 — Norm
X = np.array([
    [3,4],
    [5,12],
    [8,15]
])
print(np.linalg.norm(X,axis=1))



## Practice 4
X = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [2,4,6]
])
w = np.array([
    [0.5],
    [1.0],
    [-0.5]
])
b = 2
prediction = X @ w + b
# 1. X.shape = 4,3
# 2. w.shape = 3,1
# 3. X @ w shape = 4,1
# 4. Why does adding scalar b work? - because b diamention is 1 
# 5. prediction.shape = 4,1
print(prediction)
print(prediction.shape)





# Practice 6 — Solve equations
# 3x + 2y = 16
# x  +  y = 6

A = np.array([
    [3,2],
    [1,1]
])
B = np.array([16,6])
solution = np.linalg.solve(A,B)
print(solution)



## practice 7 
# 2x + 3y = 13
# 4x +  y = 11

C = np.array([
    [2,3],
    [4,1]
])
D = np.array([13,11])
soln = np.linalg.solve(C,D)
print(soln)