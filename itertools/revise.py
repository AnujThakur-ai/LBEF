from itertools import *

#count --> infinite counting so we need break to terminate the loop
print('count:')
for i in count(10, 3):
    if i > 30:#ending statement
        break
    else:
        print(i)
        
        
        
#cycle ---> it will rotate the given iterable items in a circle manner
print('\ncycle:')
l = cycle(['A', 'B', 'C'])

for _ in range(10):
    print(next(l))


#repeat --> it will repeat the given item for specified number of times
print('\nrepeat:')
r = repeat ('anuj', times = 5)
print(list(r))

#using for loop
print('\nrepeat using for loop:')
for i in repeat( 'anuj', times = 5):
    print(i)
    
#chain --> it will combine multiple iterables into a single iterable
print('\nchain:')
c = chain (['anuj', 3, 'b'], [4, 5, 6])
print(list(c))

#zip_longest --> it will combine multiple iterables into a single iterable but it will fill the missing values with specified fillvalue
print('\nzip_longest:')
z = zip([1,2,3], ['a', 'b', c])
print(list(z))
#it sometimes give error if the length of iterables are not same or dangerous to use it may loss some data

z1 = zip_longest([1,2,3,4,5], ['a', 'b', 'c'], fillvalue= '0')
print(list(z1))