#week-days via match-case
#code

day = int(input('Enter 1-7: '))

#using match-case

match day:
	case 1:
		print('Sunday')
	case 2:
		print('Monday')
	case 3:
		print('Tuesday')
	case 4:
		print('Wednesday')
	case 5:
		print('Thrusday')
	case 6:
		print('Friday')
	case 7:
		print('Saturday')
	case _:
		print('Invalid Input!!,\n enter 1-7 only!!')

