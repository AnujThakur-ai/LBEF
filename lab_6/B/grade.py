# function to print the grade of student

#mark function
def mark():
    marks = []
    while True:
        m = eval(input('Enter mark: '))
        if m >=0 and m <= 100:
            marks.append(m)
        else:
            print('Wrong Input!!!')
        
        per = input('Do you wnat to enter another subject marks(y/n):')
        
        if per.lower() !='y':
            break
    total = 0
    for i in marks:
        total+=i
        
    a = avg(total, marks)
    grade = grade_result(a)
    return total, a, grade

#average

def avg(total, l: list):
    
    average = total / len(l)
    return average
    
#grade_result
def grade_result(average):
    if average <= 100 and average >= 80:
        return 'A+'
    elif average < 80 and average >= 75:
        return 'A'
    elif average >=70 and average <=74:
        return 'B+'
    elif average >=65 and average <= 69:
        return 'B'
    elif average >= 60 and average <= 64:
        return 'C+'
    elif average >= 55 and average <= 59:
        return 'C'
    
    elif average >= 50 and average <= 54:
        return 'C-'
    elif average >= 40 and average <= 49:
        return 'D'
    elif average >= 0 and average <= 39:
        return 'F'
    else:
        return 'None'
    
#display
def display(name, roll, result): 
    print(f'Name: {name}\nTP_NUMBER:{roll}\nYour Result: {result}')

#name, subjects marks, tp number


name = input('Enter Name: ')

tp_num = int(input('Enter TP Number: '))

result = mark()

d = display(name, tp_num, result)

print(d)

     
    

        


 

