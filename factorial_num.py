#to print the factorial number 

#code

#user-choice

user = int(input('Enter number: '))

#using while Loop 

if user < 1: 
    print('Invalid Input!!, Try again later!!')
else:   
    result = 1
    while user > 1: 
        result *=user
        user -=1
    print('Result: ', result)
        
    