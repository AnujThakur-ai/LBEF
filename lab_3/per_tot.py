# take 5 subs mark and calculate tota and percent

mark1 = eval(input('Enter 1st subject mark: '))
mark2 = eval(input('Enter 2nd subject mark: '))
mark3 = eval(input('Enter 3rd subject mark: '))
mark4 = eval(input('Enter 4th subject mark: '))
mark5 = eval(input('Enter 5th subject mark: '))

obt_mark = mark1+ mark2 + mark3 + mark4 + mark5 

percentage = (obt_mark/500)*100

print(f'obtained mark: {obt_mark}\npercentage: {round(percentage,2)}%')


