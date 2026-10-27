import numpy as np

ages = np.array([[14,23,54,34,53,26,70,43],
[37,29,11,21,10,14,67,45]])


#teenagers = ages[ages<18]
#adults =ages[ages>=18]
#print(teenagers)
#print(adults)

adults = np.where(ages>=18,ages,0)
print(adults)