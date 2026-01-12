# set pratice


# empty set 

d = {}
print('type of d :', type(d)) # dict

s = set()
print('type of s: ', type(s))# set


# set is mutable
# for i in dir(set):
#     print(i)

#to check for disjoint

s1 = {1, 2, 3, 4, 5}
s2 = {2,3 , 4, 5,6}
print(f's1: {s1}\ns2 : {s2} ')
# notion
print('is s1 disjoint set with s2: ',s1.isdisjoint(s2))

#union 
print('union of set 1 and set 2: ', s1 | s2) 
 
#intersection
print('intersection of set 1 and s2: ', s1 & s2)

#methods
print('union of set 1 and s2 : ', s1.union(s2))
print('Intersection of set 1 and set 2: ', s1.intersection(s2))

print('difference of s1 and s2: ', s1 - s2)
print('difference of s2 and s1: ', s2 - s1)


print('Difference of s1 and s2: ', s1.difference(s2))


# additon of set
# print('addtion of set 1 and s2:  ', s1 + s2)--> this operand is not valid in set

# #method
# print('add: ',s1.__add__(s2))
s1.add(100)
print('add method: ', s1)


# pop last element of s2

s2.pop()# pop donot takes any argumennt, it iteself remove the first item from the set
print('pop element: ', s2)

#difference in list
l = [ 2, 3, 4]
print('list: ', l)
l.pop()
print('pop in list: ',l)


#remove 
#--> it remove the specified element from the set but if item is not available then throw an error

s1. remove (100)
print('s1 after removing 100 item: ', s1)

# using discard

s1.discard(100)
print('s1 trying to remove 100 using discard: ', s1)# it does not throw any error if the element  is no tpresent

# trying to remove 101 from s1 using remove 
# s1.remove(101) # -- > throw an error
# print(s1)
#   File "/home/anuj/set_pratice.py", line 75, in <module>
#     s1.remove(101) # -- > throw an error
#     ^^^^^^^^^^^^^^
# KeyError: 101


a, b, c, d, e = s1
print('Unpacking the items from set 1:')
print(a, b, c, d, e)

