from itertools import count
# count = itertools.count(start=0, step=1)
for i in count ( 10, 2):
    if i > 20:
        break
    else:
        print(i)
    