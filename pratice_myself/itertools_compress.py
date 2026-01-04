# itertools compress() example
from itertools import compress
l  = ['A', 'B', 'C', 'D', 'E']
l1 =[True, False, True, False, True]

result = compress(l, l1)
print(f'Compressed result: {list(result)}')