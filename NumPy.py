import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Array:- ",arr1)

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:- \n",arr2)

print("Shape Of Arr2:- ", arr2.shape)
print("Elements In Arr2:- ", arr2.size)

print("--------------------------\n Slicing")
a1 = np.array([4,7,9,10,12,14,16,18,19,20])
print(a1[2])
print(a1[-2])
print(a1[1:4])
print(a1[2:])
print(a1[:5])
print(a1[1:4:2])
print(a1[::2])