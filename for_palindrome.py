# check the palidrome using for loop

num = int(input('Enter Number: '))

for n in range(2, num):
	if num % n == 0:
		print(f'{num} is not palindrome!!')
		break
else:
	print(f'{num} is palindrome')
