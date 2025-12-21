# to print the fibonacchi series

first = 0
second = 1

# take input
num  = int(input('Enter number: '))
print('Fibonacchi series: ')

print(first)
print(second)

i = 3
while i <= num:
	third = first + second
	print(third)
	first = second
	second = third
	i += 1
else:
	print('invalid number')

