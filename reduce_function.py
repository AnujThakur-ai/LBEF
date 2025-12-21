#reduce function

from functools import reduce

l = [1,2,3,11,22,44,112,453,123,55,345,645]
addd = (reduce(lambda x, y: x + y, ll))
print("sum of list elements:", addd )

mult = reduce(lambda x, y: x* y, l)
print("product of list elements: ", mult)

maxx = reduce (lambda x, y: x if x>y else y, l)
print("maximum element in the list: ", maxx)

minn = reduce (lambda x, y: x if x < y else y, l)
print("minimum element in the list: ", minn)