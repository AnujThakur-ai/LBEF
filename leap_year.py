'''

LEAP YEAR LOGIC
1. DIVIDE BY 4 IF TRUE
2. DIVIDE BY 100 IF TRUE
3. DIVIDE BY 400 IF TRUE
MEANING : LEAP YEAR
ELSE
MEANING : NOT A LEAP YEAR
2000 % 4 == 0: TRUE
2000 % 100 == 0: TRUE
2000 % 400 == 0: TRUE
2000 IS LEAP YEAR
'''


#CODE
year = int(input('enter year: '))

if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 == 0:
            print(f'{year} is leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')