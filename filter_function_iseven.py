#filter function


l = [1,2,3,11,22,44,112,453,123,55,345,645]
l1 = filter(lambda x : x%2 ==0, l)
print(list(l1))