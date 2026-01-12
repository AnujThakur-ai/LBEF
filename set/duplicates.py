# to remove duplicates from a list while preserving the order of first occurrences
l = [ 1,2,2,3,4,3,4,21,32,44,2,1,2,3,4,4,5,6]
d = list(dict.fromkeys(l))
print(d)


print('2nd method to remove duplicates using collections.Counter')
from collections import Counter
l = [ 1,2,2,3,4,3,4,21,32,44,2,1,2,3,4,4,5,6]
d = Counter(l)
print(list(d.keys()))
