import numpy as np 
X = np.array([
    [1,2,3],
    [4,5,6]
])
X= X.astype(dtype=np.int32)
print(X.dtype,X.shape,X.ndim)

np.save("X.npy",X)  # to save single array .npy
loaded_X = np.load("X.npy")
print(loaded_X)
print(loaded_X.dtype,loaded_X.shape,loaded_X.ndim)

# .npy preserves the NumPy structure directly.

## Save multiple array
X_train = np.array([1,8,9])
X_test = np.array([1,8,9])
y_train = np.array([1,8,9])
y_test = np.array([1,8,9])

np.savez("dataset.npz",            # savez and .npz for multiple 
        X_test = X_test,
        X_train = X_train,
        y_test = y_test,
        y_train = y_train)
data = np.load("dataset.npz")
print(data["X_train"])
print(data.files)



## Save as text
np.savetxt("X.txt",X,fmt="%d")
txt_X = np.loadtxt("X.txt")
print(txt_X)



## Save CSV
# np.savetxt("X.csv",X,fmt="%d",delimiter=",")  
# csv_X = np.loadtxt("X.csv",delimiter=",",     
#                    dtype=np.float32)  ## ## np.loadtxt() can struggle with missing values.
# print(csv_X)


## genfromtxt() - can handle missing value better  --Missing numeric values can become: nan    
csv_x = np.genfromtxt("X.csv",
                      delimiter=",",
                      skip_header=1, # skip 1st row 
                      usecols=(0,1) # select column 
                      )  
print(csv_x)


## with loadtxt() - skiprows = 1, with genfromtxt() - skip_headers = 1


