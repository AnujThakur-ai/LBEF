i = 1
m = 0
avg = 0
while True:
	name = input('name or (stop to exit): ')
	if name.lower() == 'stop':
		break
	score = eval(input('score: '))
	
	if score in range(1,101):
		m +=score
		avg = m/i
		
	i += 1

print('avg' , avg)
		

