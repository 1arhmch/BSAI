import numpy as np

arr = np.array([
[1,2,3,4],
[5,6,7,8],
[9,10,11,12],
[13,14,15,16]
]

)
b1  = arr[0:3,0:3]
b2 = arr[1:3,1:3]
b3 = arr[1:,1:]
print(arr)
print()
print(b1)
print()
print(b2)
print()
print(b3)