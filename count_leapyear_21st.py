# to count the total number leap year in the 21st century

start = 2000
end = 2100

count_leapyear = 0
while start <=end:
	if ( start % 4== 0) and (start % 400 == 0 or start % 100 !=0):
		print(start)
		count_leapyear +=1
	start +=1
print(f'total years are {count_leapyear}')