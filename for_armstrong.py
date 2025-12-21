# to check the number is armstrong num or not

num = int(input('Enter number: '))
original = num
num_str = str(num)

armstrong = 0
if num > 0:
	for n in range(len(num_str)):
		rem = num % 10
		armstrong = armstrong + rem ** len(num_str)
		num = num // 10
	if armstrong == original:
		print('Armstrong number!!')
	else:
		print('not armstrong!!')
else:
	print('Invalid Number!!')