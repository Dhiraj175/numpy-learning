import numpy as np

rng = np.random.default_rng()

print(rng.integers(1,12))   # 12 excluded 
print(rng.integers(1,12,size=5))  ## size - output shape - 5,
print(rng.integers(1,12,size=[4,2]))  ## size - output shape -- 4,2

# Random floating-point numbers
print(rng.random())
print(rng.random(5))  # 5 values

# Random matrix
print(rng.random([3,4]))

# uniform
print(rng.uniform(5,25,size=2))


# Normal distribution - 
print(rng.normal(
    loc = 0.1,  # mean
    scale = 0.001, # std deviation
    size = 5 # shape
))


## Reproducibility -
# rng = np.random.default_rng(42)


## choice() — random sampling
student = np.array(["A","B","C","D","E"])
print(rng.choice(student))
print(rng.choice(student,size=3))  #  value can appears twice or more 
print(rng.choice(student,size=3,replace=False)) # unique


# shuffle() vs permutation()
rng.shuffle(student)  ## modify array itself
print(student)

print(rng.permutation(student)) # return shuffle copy





# =============================================================
# Practice
# =============================================================
rng = np.random.default_rng(42)
x = rng.normal(
    loc = 0,
    scale=1,
    size=(100,5)
)
y = rng.integers(0,2,100)
print(x,y)



## Practice 1 — Random basics

# Generate one integer from 1 through 10.
print(rng.integers(1,10))

# Generate 10 integers between 0 and 100.
print(rng.integers(0,100,10))

# Generate a (3,4) integer matrix from 1 through 50.
print(rng.integers(1,50,(3,4)))

# Generate five floating-point numbers between 0 and 1.
print(rng.random(5))

# Generate a (2,3) float matrix between 0 and 1.
print(rng.random((2,3)))

# 100 values uniformly distributed between 10 and 50.
print(rng.uniform(10,50,100))

# 500 values from a normal distribution with: mean = 100 & std = 15
data = (rng.normal(
    loc = 100,
    scale = 15,
    size = 500
))


# Print the generated normal data's:
print(np.mean(data))
print(np.std(data))



# Practice 3 — Choice
products = np.array([
    "Laptop",
    "Phone",
    "Watch",
    "Camera",
    "Tablet"
])
# Pick one product.
print(rng.choice(products))

# Pick 3 products allowing duplicates.
print(rng.choice(products,3))

# Pick 3 products without duplicates.
print(rng.choice(products,3,replace=False))

# Pick 10 products using probabilities: Laptop → 0.10
# Phone  → 0.40
# Watch  → 0.20
# Camera → 0.10
# Tablet → 0.20

print(rng.choice(
    products,
    size=10,
    p=[0.10,0.40,0.20,0.10,0.20]
))




## practice 6
x = rng.normal(
    loc=0,
    scale=1,
    size= (200,4)
)
y= rng.integers(0,2,200)
print(y)
indices = rng.permutation(len(y))
x_shuffled = x[indices]
y_shuffled = y[indices]