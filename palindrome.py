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

if rev == n:
	print(f'Num {n} is palindrome.')
else:
	print(f'num {n} is not a palindrome number.')
