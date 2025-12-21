#map function
l = [1,2,3,11,22,44,112,453,123,55,345,645]
l1 = list(map(lambda x: x*2, l))
print("doubled list: ", l1)

l2 = list(map(lambda x: x**2, l))
print("squared list: ", l2)

l3 = list(map(lambda x: x+5, l))
print("add 5 to each element: ", l3 )