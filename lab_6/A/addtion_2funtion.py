'''
1. a outer function 
2. a inner function which sum a and b
3. outer function will add 5 to inner function and return it.
'''


def outer_fun(y, z):
    
    #inner function
    def inner_fun(y, z):
        return y+z
    
    rest = inner_fun(y, z)
    
    print('Result : ',rest + 5)


# outer_fun(3, 3)
a, b = map(int, input('Enter 2 numbers: ').split())

outer_fun(a, b)