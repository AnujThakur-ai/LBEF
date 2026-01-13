#repeat
from itertools import repeat
# repeat = itertools.repeat(object, times=None)
for i in repeat('Hello', 5):
    print(i)
    
# This program will print 'Hello' 5 times. If times is not specified, it will repeat infinitely.
# To avoid infinite loop, we can use islice from itertools to limit the output
