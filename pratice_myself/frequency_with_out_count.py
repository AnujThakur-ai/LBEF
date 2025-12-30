'''
Q2

Without using count():

Find the frequency of each element in a list
'''
#take a list of integers    
from collections import Counter
l = []
#ask for user how many elements to be added in list\
n = int(input('How many elements you want to add in list: '))
for num in range(n):
    element = eval(input('Enter element: '))
    l.append(element)
#frequency of each element in list
frequency = Counter(l)
print(frequency, end = '\n')