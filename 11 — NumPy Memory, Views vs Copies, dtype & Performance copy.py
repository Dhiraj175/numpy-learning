import numpy as np

a = np.array([10,20,30,257])
b = a
b[0] = 25    # Changing b changed a
print(b)
print(a)
print(a is b)
print(np.shares_memory(a,b))
c= a[:2]  # Slicing usually creates Views
print(np.shares_memory(a,c))
d = a.copy()
print(np.shares_memory(a,d))  ## independent copy different object different memory



# Basic slicing
# a[1:4]
# → usually VIEW


# Fancy indexing
# a[[1,3]]
# → COPY


# Boolean indexing
# a[a > 20]
# → COPY



# ravel() vs flatten()
# ravel tries to return view & flatten always copy
a=[1]
for i in range(3):
    a.append(a[-1]*2)
print(sum(a))