def add_emp():
    emp = []
    #add emp
    n = 0
 
    while n <3:
        d={
       'name' : [],
       'age' : [],
       'email' : [],
       'post' : [],
       'salary' : []
       
    }  
        name = input('Enter name: ')
        d['name'] = name
        age = int(input('Enter age: '))
        d.update(d[age])
        email = input('Enter email: ')
        d.update(email)
        post = input('Enter post: ')
        d.update(post)
        salary = float(input('Enter salary: '))
        d.update(salary)
        
        emp.append(d)
        n+=1
add_emp()   