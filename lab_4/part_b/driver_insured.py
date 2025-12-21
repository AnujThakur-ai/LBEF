# if the driver is insured or not

martial_status = int(input('Enter Marital Status:(1 for yes, 2 for no): '))
if martial_status == 1:
	print('Insured')
elif martial_status == 2:
	age = int(input('Enter age: '))
	sex = int(input('enter 1 for female and 0 for male: '))


	if sex == 0:
		if age > 35:
			print('insured')
		else:
			print('not insured')
	elif sex == 1:
		if age > 25:
			print('Insured')
		else:
			print('not insured')
	else:
		print('Invalid')

else:
	print('invalid')