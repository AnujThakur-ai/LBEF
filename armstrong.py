#take input 
user = int(input('Enter the num: '))

# copy the value
num = user
l = len(str(user))


#initilize 
summ = 0

while num > 0:
	rem = num % 10
	summ = summ + rem**l
	num //=10

if summ == user:
	print('yes')
else:
	print('no')
