import numpy as np 

a = np.array([12,4,5,3])
b = np.array([3,6.5,7,-10])

## What is a ufunc? -- universal function
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))
print(np.sqrt(a))
print(np.square(b))
print(np.abs(b))  # remove -ve sign
print(np.exp(a))
print(np.log(a))
print(np.log2(b))
print(np.log10(b))



## Trigonometric ufuncs
# np.sin()
# np.cos()
# np.tan()
angles = np.array([0,np.pi/2,np.pi])
print(np.sin(angles))



## Maximum and minimum element-wise
a = np.array([12,4,5,3])
b = np.array([3,6.5,7,-10])

print(np.max(a))  # one maximum from array
print(np.maximum(a,b))  # element-wise comparison
print(np.minimum(a,b))



# np.clip()
scores = np.array([-20,10,50,120])
# want values limited to:0 to 100
print(np.clip(scores,0,100))



## Comparison ufuncs
a = np.array([10,20,30])
b = np.array([15,20,25])
print(np.greater(a,b))
# np.less()
# np.equal()
# np.not_equal()
# np.greater_equal()
# np.less_equal()



## logical ufunc
age = np.array([17,21,30,16])
score = np.array([80,70,95,88])
print(np.logical_and(age>18,score>=70))
print((age>18)&(score>=70))

# np.logical_or()
# np.logical_not()
# np.logical_xor()



## Rounding functions
x = np.array([1.2,2.7,3.5,4.9])
print(np.round(x))
print(np.floor(x))  #lower
print(np.ceil(x))   # HIGHER
print(np.trunc(x))




## np.isnan()   --- check missing numeric values:
data = np.array([4,np.nan,2,np.nan])
print(np.isnan(data))  
print(data[np.isnan(data)])
print(data[~np.isnan(data)])  # non nan
print(np.mean(data))  # give nan output
print(np.nanmean(data))
# np.nansum()
# np.nanmin()
# np.nanmax()
# np.nanmedian()
# np.nanstd()


## Infinity & isinf()
data = np.array([2,9,np.inf,7,np.inf])
print(np.isinf(data))
print(data[~np.isinf(data)])
print(np.isfinite(data))  # check valid finite number


## Chaining vectorized operations
X = np.array([
    [1,2],
    [3,4],
    [5,6]
])
result = np.sqrt(X*2+5)  # X * 2 --> +5 ---> square root
print(result)




#==============================================================
# Practice
#==============================================================

## Practice 1 — Basic ufuncs
a = np.array([4,9,16,25])
# 1. square root of every value
print(np.sqrt(a))

# 2. square every value
print(np.square(a))

# 3. log of every value
print(np.log(a))

# 4. absolute values after doing a - 20
print(np.abs(a-20))


## Practice 2 — Maximum / minimum
a = np.array([10,50,30,80])
b = np.array([20,40,35,70])
# 1. element-wise maximum
print(np.maximum(a,b))

# 2. element-wise minimum
print(np.minimum(a,b))

# 3. maximum of entire a
print(np.max(a))



## Practice 3 — Missing values
data = np.array([
    10,
    np.nan,
    30,
    40,
    np.nan,
    60
])
# 1. Find where NaN values exist.
print(np.isnan(data))

# 2. Remove NaN values.
print(data[~np.isnan(data)])

# 3. Calculate mean ignoring NaN.
print(np.nanmean(data))

# 4. Count how many NaNs exist.
print(len(data[np.isnan(data)]))
print(np.count_nonzero(np.isnan(data)))  ## Better version
print(np.sum(np.isnan(data)))   ## better version 


## Practice 4 — Vectorized classification
marks = np.array([
    35,48,52,67,74,83,91
])
# without loop
# < 50     → Fail
# 50–74    → Average
# >= 75    → Good
# >= 90    → Excellent
conditions = [
    marks >= 90,
    marks >= 75,
    marks >= 50,
]
choice = [
    "Excellent",
    "Good",
    "Average",
]
print(np.select(
    conditions,
    choice,
    default= "Fail"
))



## Practice 5 — Vectorized error
y_true = np.array([10,20,30,40,50])

y_pred = np.array([12,18,29,45,47])

# 1. error
error = y_pred-y_true
print(error)

# 2. absolute error
print(np.abs(error))

# 3. squared error
print(np.square(error))

# 4. mean absolute error
print(np.mean(np.abs(error)))

# 5. mean squared error
print(np.mean(error ** 2))



## Practice 6 — Data cleaning
data = np.array([
    25,
    np.nan,
    120,
    -15,
    80,
    np.inf,
    45
])
finite_val = np.isfinite(data)
# 1. Find finite values.
print(finite_val)

# 2. Remove NaN and infinity.
print(data[finite_val])

# 3. Clip remaining values between 0 and 100.
cleaned_data = np.clip(data[finite_val],0,100)
print(cleaned_data)

# 4. Calculate cleaned mean.
print(np.mean(cleaned_data))




## Final AIML Challenge
X = np.array([
    [10,100,1000],
    [20,200,2000],
    [30,300,3000],
    [40,400,4000]
], dtype=float)

# 1. Calculate feature-wise mean.
print(np.mean(X,axis=0))

# 2. Calculate feature-wise std.
print(np.std(X,axis=0))

# 3. Standardize X.
X_standardize = (X-np.mean(X,axis=0))/(np.std(X,axis=0))
print(X_standardize)

# 4. Take absolute values of standardized data.
abs_value = np.abs(X_standardize)
print(abs_value)

# 5. Clip all values to maximum 1.
X_clipped = np.clip(abs_value,0,1)
print(X_clipped)

# 6. Find which elements are >= 0.5.

print(X_clipped >= 0.5)

# 7. Count how many elements satisfy that condition.
print(np.count_nonzero(X_clipped>=0.5))