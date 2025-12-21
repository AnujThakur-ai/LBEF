# to take input and print grade

# mark
m = eval(input('Enter mark : '))

# condition
if m > 80:
	print('A')
elif m > 60 and m <= 79:
	print('B')
elif m > 40 and m <=59:
	print('C')
else:
	print('D')
