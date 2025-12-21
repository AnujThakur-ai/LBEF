# to check if the number is in a range or not

n = int(input('Enter num : '))

num = [n for n in range(1, 1000)]

if n in num:
	print(f'{n} is in range')
else:
	print(f'{n} is not in range.')

		