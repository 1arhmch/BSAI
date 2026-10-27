import numpy as np

arr = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
])

print(np.sum(arr,axis=0)) #sum of each column
print(np.sum(arr,axis=1)) #sum of each row
print(np.sum(arr)) #sum of all elements
print(np.mean(arr,axis=0)) #mean of each column
print(np.mean(arr,axis=1)) #mean of each row
print(np.mean(arr)) #mean of all elements