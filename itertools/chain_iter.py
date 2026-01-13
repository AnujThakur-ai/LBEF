# chain combine  multiple iterables into a single sqquence safely
from itertools import chain
# chain = itertools.chain(*iterables)
a = [1,2,3]
b = ('x','y','z')
c = {'name':'Alice', 'age':30}
for item in chain(a, b, c):
    print(item)
# This will print elements from list a, then tuple b, then keys from dictionary c in order  