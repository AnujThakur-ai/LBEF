from random import *

# Generate 5 account numbers, each 16 digits long
for i in range(5):
    acc = [randint(0,9) for _ in range(16)]
    print(''.join(map(str, acc)))

