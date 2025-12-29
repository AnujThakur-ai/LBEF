#list function in list

#list method


l = [1,2,3,1,2,412,4,123]

#list append
l.append(100)

print('list append\n',l)

#shallow copy of the list

a = l.copy()
print('\nShallow copy of list\n:',a)

#list count
print('\nlist count\n:',l.count(2))


#list extend()
l.extend([2,3,54,55,56])
print('\nextended list:\n',l)

#list index()

print('\nindex of 2:',l.index(2))

#list pop it will remove the last element of list
print('\nPop:\n', l.pop())

#remove element from list
l.remove(2)
print('\nRemove Element:\n',l)


#reverse the list
l.reverse()
print('\nReverse list:\n',l)

#sort element of the list
l.sort()
print('\nSorted list:\n',l)

#insert into specified position
l.insert(2, 99)
print('\nInserted 99 in index 2:\n',l)

#clear the list
l.clear()
print('\nCleared List:\n',l)

