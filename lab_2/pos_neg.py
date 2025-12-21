# to print the number is +ve , -ve or zero

num = int(input('Enter number: '))

# logic

if num == 0:
	print('You have entered 0!!!')
elif(num > 0):
	print(f'{num} is positive!!')
else:
	print(f'{num} is negative!!')
