# to print the number divisable by 5 and 6 in between 1 to 500

#code

start = 1
end = 500
count = 0
while start <=500:
	if start % 5 == 0 and start % 6 == 0 :
		print(start)
		count +=1
	start +=1
print(f'The total numbers divisiable by 5 and 6 between 1 to 500 are {count}')