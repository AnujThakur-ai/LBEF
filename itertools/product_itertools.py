from itertools import product


#product --> use to get the cartesian product of input iterables
print('product:')
p = product ('AB', '12')
print(list(p))
#output: [('A', '1'), ('A', '2'), ('B', '1'), ('B', '2')]

p1 = product ([2,6], [6,7])
print(list(p1))


p2 = product ([33,11], [100, 'a'])
print(list(p2))