s = 'Hello, my name is anuj kumar thakur, and i am from sarlahi district.'

d = {}
for x in s:
    d[x.lower()] = d.get(x.lower(), 0) + 1
    
for x, y in d.items():
    print(f'{x} occurs {y} times')

#counter method
from collections import Counter

    
c = Counter(s.lower())

# take input
check = input('Enter any character: ').lower()

if check in c:
    print(f'{check} occurred {c[check]} times')
else:
    print(f'{check} did not occur')