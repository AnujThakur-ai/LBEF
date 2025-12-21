# code
num = int(input( ))

num_c = num
num_str = str(num)
arm = 0
for n in range(len(num_str)):
	rem = num % 10
	arm = arm+rem ** 3
	num = num // 10
if arm == num_c:
	print('yes')
else:
	print('no')

	