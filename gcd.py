#calculate GDC 
'''
To find Greatest Common Factor
1. take Lcm or factor of each num.
2. match the number, if found take it and multiply
3. match according 
4. display result
'''
#code
import time
#TAKE INPUT OF TWO NUMBERS
a, b = map(int, input('Enter anu 2 numbers: '). split())
t1 = time.time()
if a<1 or b < 1:
    print('Invalid Input!!')
elif a ==b: 
    print('Same Input anwer: ', a)  
else: 
    while a != b:
        if a > b: 
            a = a-b
        else:
            b = b-a
    print('gcd: ', a)
t2 = time.time()
print(f'{t2-t1} secs')