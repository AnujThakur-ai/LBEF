# prime number 

num = int(input('Enter number: '))

i = 2
prime = 'yes'
while i <= num:
	if num % i == 0:
		prime = 'No'
		break
	else:
		i += 1
	
		
if prime == 'yes':
	print(f'{num} is prime number')
else:
	print(f'{num} is not a prime number!')
