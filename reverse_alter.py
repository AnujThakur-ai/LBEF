#take input
num = int(input('Enter number: '))
#copying the orginal number for last print option
n = num
# initilizing the rev
rev = 0
#using looping condition

while num > 0:
	rem = num % 10
	rev = rev*10 +rem
	num = num // 10
print(f'reverse of {n} is {rev} : ', rev)