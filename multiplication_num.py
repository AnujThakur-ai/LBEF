# to print the multiplication table of given number

#code

#user
num = eval(input('Enter any number: '))
start = 1
while start <= 10:
	print(f'{num} X {start} = {num *start}')
	start += 1
