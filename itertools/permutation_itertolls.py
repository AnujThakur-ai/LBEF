from itertools import permutations

'''
permutation: where orders matter
it uses formula: p (n , r) = n!/(n-r)!.
if it is in a cycle it will use formula : (n-1)!



'''

print('Permutation: ')

p = ([1,2], [3,4])
for i, value in permutations(p):
    print(f'{i}')