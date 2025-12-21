def emp(name, salary):
    if salary == '':
        print(f'output:\nName:{name}\nSalary:{9000}')
    else:
        salary = float(salary)
        print(f'output:\nName:{name}\nSalary:{salary}')
    
    
    
name = input('Enter name: ')
sal = input('Enter salary: ')

result = emp(name, sal)
print(result)
        
