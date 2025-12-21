#menu-driven program
'''
---> for simple calculator using match-case.
--->
'''

print('\n Menu\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Divide \n 5. power \n 6. reminder \n 7. even-odd \n 8. prime-number\n')

#code based on menu
#function to take input
def take_input():
	a = int(input('Enter first Number: '))
	b = int(input('Enter Second Number: '))
	return a, b

#take order
order = int(input('Enter your Order (1-8): '))

match order:
	case 1:
		a, b = take_input()
		print(a+b)
	case 2:
		a,b =take_input()
		print(a-b)
	case 3:
		a, b = take_input()
		print(a*b)
	case 4:
		a, b = take_input()
		print(a/b)
	case 5:
		a, b = take_input()
		print(a**b)
	case 6:
		a, b = take_input() 
		print(a % b )
	case 7:
		#even-odd
		a = int(input('enter number : '))
		if a % 2 == 0:
			print(f'{a} is Even')
		else:
			print(f'{a} is Odd')
	case 8:
		#prime-number
		num = int(input('Enter number : '))
		for n in range(2, int(num ** 0.5) +1):
			if num % n == 0:
				print(f'{num} is not a prime number')
				break
		else:
			print(f'{num} is a prime number')

		
	case _:
		print('Not Availabel!!')
		