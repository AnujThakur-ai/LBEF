from itertools import cycle
# cycle = itertools.cycle(iterable)
c = cycle([1,2,3])
for _ in range(10):
    print(next(c))
    
# print the data for 10 times means it will print 1,2,3,1,2,3,1,2,3,1, iterable times means it will print infinite times