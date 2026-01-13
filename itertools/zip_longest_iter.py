#zip()--> siltely drops the data
print('using zip only: ')
print(list(zip([1, 2, 3], [10])))


from itertools import zip_longest
print('usoing zip_longest from itertools:')
print(list(zip_longest([1, 2, 3], [10]))) # [2, none] because fillvalue is not presernt
print('zip longest with fillvalue = 0: ')
print(list(zip_longest([1,2,3], [11], fillvalue = 0)))