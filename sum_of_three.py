#take input 
user = int(input('Enter the num: '))

# copy the value
num = user

#initilize 
summ = 0

while num > 0:
	rem = num % 10
	summ += rem
	num //=10
print('sum : ', summ)
