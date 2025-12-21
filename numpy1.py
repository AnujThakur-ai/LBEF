import numpy as np 

#praticing numpy tutorial 

#code

# two different array

arr1 = np.array([1,2,3,4,5,6,7,8,9,10])
arr2 = np.array([11,12,13,14,15,16,17,18,19,20])

#copy vs view

a = arr1.copy()
b = arr1.view()

# print the base, to check whether it's orginal or new array list

print('base of a.copy: ',a.base)
print('base of a.view: ',b.base)


#reshape the arrary from 1d to 2d

newarr = arr1.reshape(5,2)
print('reshape into 2d: ',newarr)
print('dimensions of newarr: ',newarr.ndim)

#reshape into 3d
#newarr1 = arr1.reshape(1,2,3)
#print('reshape into 3d: ', newarr1) reason to get failed in this 

#looping thorough this values
print('using normal for loop: \n')
for x in arr1:
	print(x)

print('usite nditer(): \n')
for x in np.nditer(newarr):
	print(x)


#concatination or joining of two arr into one 

c = np.concatenate((arr1, arr2))
print('concatinate: \n', c)

#concatenated via stack function

d = np.stack((arr1, arr2), axis = 0) # via columns
print('concatinate via stack by col: \n', d)

e = np.stack((arr1, arr2), axis = 1) # via rows
print('concatinate via stack by col: \n', e)