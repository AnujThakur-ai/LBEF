#WA FUNCTION NAME ADD_EMP WITH ADD ALLEAST 20 EMPLOYEE DETAILS, id, NAME, AGE, EMAIL, DESIGNATION, SALARY

#wap function named display employee(), which prints all the emp details

# function named search_employee(), which finds employee information based on their id, if emp not found the print
#message emp details not found


l = []
def add_emp():
    
    for i in range(3):
        emp = {} # empty dict
        ids = int(input('enter ids: '))
        name = input('enter name: ')
        age = int(input('Enter age: '))
        sal = float (input('enter salary : '))
        em = input('Enter email: ')
        des = input('enter post: ')
        print('-' * 30)
        emp['name'] = name
        emp['ids'] = ids
        emp['age'] = age
        emp['salary'] = sal
        emp['email']  =  em
        emp['designation '] = des
        l.append(emp)
        
def display (l: list):
    for i in l:
        print(i)
        
add_emp()
display(l)
            