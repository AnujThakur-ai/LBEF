# calculating gcd using elucidiean meathod
a, b = map(int, input('enter 2 number: ').split())

#logic
import time
t = time.time()
if a<1 or b < 1:
    print('Invalid Input!!')
    
else:
    while b!=0:
        temp = b
        b = a%b
        a = temp
print('gcd : ', a)

m = time.time()
print(f'{m - t} secs')