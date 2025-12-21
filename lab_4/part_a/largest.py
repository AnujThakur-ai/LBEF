# to print the largest number between 3 numbers

# take 3 numbers
a = eval(input('Enter first: '))
b = eval(input('Enter 2nd : '))
c =eval(input('Enter  3rd: '))

if a > b and a > c:
	print(f'{a} is greater!!')
elif b > a and b > c:
	print(f'{b} is greater!!')
else:
	print(f'{c} is greater!!')