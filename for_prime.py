num = int(input('enter number: '))

if num <= 1:                         
    print('not prime number')
else:
    for n in range(2, num):            
        if num % n == 0:
            print('not prime number')
            break
    else:
        print('Prime number')
