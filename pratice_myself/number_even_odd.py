'''
Q1

Write a program to:

Take a list of integers

Create a new list of tuples (number, "even"/"odd")
'''

#take a list of integers
l = []

#ask for user how many elements to be added in list\
n = int(input('How many elements you want to add in list: '))
for num in range(n):
    element = eval(input('Enter element: '))
    l.append(element)
    
#even odd list
even_odd = [(i, "even" if i % 2 == 0 else "odd") for i in l]
print(even_odd, end = '\n')