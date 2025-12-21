#filter function


l = [1,2,3,11,22,44,112,453,123,55,345,645]
l1 = filter(lambda x : x%2 ==0, l)
print("is even: ", list(l1))

l2 = filter(lambda x : x%2 !=0, l)
print("is odd: ", list(l2))

l3 = list(filter(lambda X: X > 100, l))

print("greater than 100: : ", l3)