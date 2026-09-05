import numpy as np

## Sorting 

arr = np.array([50,70,20,34,96,15])
print(np.sort(arr))    ## return new sorted arr
print(arr)

arr.sort()   ## sort original array
print(arr)


## Decending sorting 
print(np.sort(arr)[::-1])


## 2D sorting 
A = np.array([
    [30,10,20],
    [90,50,70],
    [60,40,80]
])

print(np.sort(A))
print(np.sort(A,axis=0))  ## Sort each column independently.
print(np.sort(A,axis=None))  ## flatten sort all values together 


## argsort()
score = np.array ([ 50,97,34,79,35,94])
print(np.argsort(score))


## np.where()   -- searching based on condition
print(score>50)
print(score[score>50])   ## boolean mask - gives matching values
print(np.where(score>50))   # return indices - matching position
print(np.where(score>40, "Pass","Fail"))  # np.where(condition, value_if_true, value_if_false)

# Multiple condition
# 1. Nexted loops
print(np.where(score>90, "A",
               np.where(score>70,"B",
                        np.where(score>40,"Pass","Fail"))))

# 2 np.select()
conditions = [
    score >= 90,
    score >= 80,
    score >= 70,
    score >= 60,
    score >= 40
] 
choices = [
    "A",
    "B",
    "C",
    "D",
    "E"
]
result = np.select(conditions,
          choices,
          default= "Fail")

print(result)



# np.nonzero()
arr = np.array([1,5,0,7,0,9,6,0])
print(np.nonzero(arr))
print(np.count_nonzero(arr))

print(np.nonzero(arr>5))


# unique values
arr = np.array([10,20,10,40,20,30,10,50,40,10])
print(np.unique(arr))
# unique value with count
value, count = np.unique(arr,return_counts=True)
print(value,count)
value, index = np.unique(arr, return_index=True)   # unique value first appeared
print(value,index)

value, inverse = np.unique(arr,return_inverse=True)
print(value,inverse)


## Set Operations -- array can be treated like set
a = np.array([1,2,3,4,5])
b = np.array([4,5,6,7])
print(np.intersect1d(a,b))   # Intersection --- value exit in both
print(np.union1d(a,b))   #Union -- all unique values
print(np.setdiff1d(a,b))  # diff -- in a but not in b
print(np.setxor1d(a,b))  # Symmetric difference -- Values belonging to either array but not both



# np.isin()
ids = np.array([100,101,102,103,104,105])
selected = np.array([102,105,108])
print(ids[np.isin(ids,selected)])


## np.clip()  -- everything constrained between
arr = np.array([10,69,-24,45,0,-4,25,6546,351,4,46,31])
print(np.clip(arr,4,25))



## np.searchsorted()
arr = np.array([10,20,30,40,50])
print(np.searchsorted(arr,35))  ## insert at position 3 -- according to sorted arr

arr = np.array([10,20,30,30,30,40])
print(np.searchsorted(arr,40))   # normally gives the left insertion position.



# =======================================================
# Practice 
# =======================================================

classes = np.array([
    "Cat",
    "Dog",
    "Horse",
    "Bird"
])

probabilities = np.array([
    0.15,
    0.65,
    0.10,
    0.10
])

print(classes[np.argmax(probabilities)])   

indices = np.argsort(probabilities)[::-1]   ## decending order max to min
print(classes[indices[:3]])


# Practice 1 — Sorting
scores = np.array([72,95,61,88,79])

# Sort ascending.
print(np.sort(scores))

# Sort descending.
print(np.sort(scores)[::-1])

# Get indices that would sort ascending.
print(np.argsort(scores))

# Get indices for descending order.
print(np.argsort(scores)[::-1])

# Find the index of the highest score.
print(np.argmax(scores))

# Find the index of the lowest score.
print(np.argmin(scores))



## Practice 2 — Related arrays
students = np.array(["A","B","C","D","E"])
marks = np.array([75,92,68,85,88])
rank = np.argsort(marks)[::-1]

# Sort marks highest → lowest.
print(np.sort(marks)[::-1])
print(marks[rank])  # Better version 

# Return student names in the same ranking.
print(students[np.argsort(marks)[::-1]])
print(students[rank])

# Return the top 3 students.
print(students[np.argsort(marks)[::-1]][:3])
print(students[rank][:3])

# Return the top 3 marks.
print(np.sort(marks)[::-1][:3])
print(marks[rank][:3])



## Practice 4 — Unique
labels = np.array([
    1,2,1,3,2,1,3,3,2,4
])

# Unique labels.
print(np.unique(labels))

# Count of each label.
label,count = np.unique(labels,return_counts=True)
print(label,count)

# Number of unique classes.
print(len(np.unique(labels)))

# Most frequent class.
max_count = np.max(count)
print(label[count == max_count])




## Practice 5 — isin
data = np.array([
    [101, 20, 75],
    [102, 22, 88],
    [103, 19, 65],
    [104, 25, 92],
    [105, 21, 80]
])   ## ID | AGE | SCORE
selected_ids = np.array([
    102,104,105
])
# Using np.isin(), return only the complete rows belonging to those IDs
print(data[np.isin(data[:,0],selected_ids)])




## Practice 6
classes = np.array([
    "Cat",
    "Dog",
    "Horse",
    "Bird",
    "Rabbit"
])

probabilities = np.array([
    0.10,
    0.48,
    0.07,
    0.25,
    0.10
])
rank = np.argsort(probabilities)[::-1]

# 1. Highest probability.
print(np.max(probabilities))

# 2. Predicted class.
print(classes[np.argmax(probabilities)])

# 3. All class indices sorted from  highest probability → lowest.
print(rank)
# 4. Classes ranked highest → lowest.
print(classes[rank])

# 5. Probabilities ranked highest → lowest.
print(probabilities[rank])

# 6. Top 3 classes.
print(classes[rank][:3])

# 7. Top 3 probabilities.
print(probabilities[rank][:3])