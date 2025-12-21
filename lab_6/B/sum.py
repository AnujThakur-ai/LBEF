# to take two input from the user and sum them 


def add(x, y):
    a = x + y
    return a


a = eval(input('Enter first num : '))
b = eval(input('Enter 2nd num: '))


result = add(a, b)

print(f'The sum of {a} and {b} is {result}')

