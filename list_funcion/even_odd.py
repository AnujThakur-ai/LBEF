#to print even odd
e = [[i, 'even' if i % 2 == 0 else 'odd'] for i in range(1, 51)]
print(e)

# #to separate even odd
# l = [i for i in range(1, 51)]
# e = [[i, 'even'] for i in l if i % 2 == 0]
# o = [[i, 'odd'] for i in l if i % 2 != 0]
# print('\nEven numbers:\n', e)
# print('\nOdd numbers:\n', o)
