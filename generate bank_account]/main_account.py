from random import *
#for details
det = []
def details():
    
    #add 20 details
    
    for i in range(1, 3):
        detail = {}
        
        #name
        
        name = input('Enter name: \t').strip()
        while not name.isalpha() or name == '':
            print('Check your name!!!\nTry Again!!')
            name = input('Enter name: \t').strip() 
            
        
        
         #age   
        age = input('Enter Age: \t').strip()
        while age == '' or not age.isdigit():
            if int(age) <= 0:
                print('check Age!!\nTry Again!')
                age = input('Enter Age: \t').strip()
            else:
                return
             
        #salary
        while True:
            try:
                sal = float(input('Enter salary:\t'))
                
            except Exception:
                print('you typed incorrectly!!Try Again!!')
                continue
            break
        
        #address
        address = input('Enter Address: \t').strip()
        while not address.isalpha() or address == '':
            print('Check Address!!\nTry Again!!')
            address = input('Enter Address: \t').strip()
            
        #account number - ensure unique for each person
        existing_acc_nums = [d['acc'] for d in det]
        while True:
            acc_num = ''.join(str(randint(0, 9)) for _ in range(16))
            if acc_num not in existing_acc_nums:
                break
        
        detail['name'] = name 
        detail['age'] = age
        detail['salary']  = sal 
        detail['address'] = address
        detail['acc'] = acc_num
        #append into list
        det.append(detail)
        print('-'*40)   
    
def display():
    people_detail = det
    for line in people_detail:
        print(line)



def search_people():
    people = det

    #take input
    while True:
        acc_n = input('enter accout number:\t').strip()
        while acc_n == '' or not acc_n.isdigit():
            print('check account number...Try Again!!')
            acc_n = input('enter accout number:\t').strip()
            
            
        found = False
        for line in people:
            if line['acc'] == acc_n:
                found = True
                print(f"Person found: {line}")
                break
        
        if not found:
            print("Person not found!")
            continue
        
def update_details():
    update_people = det
    
    #which details wanna make change
    choice = input('1.name\n2.age\n3.address\n4.salary\nEnter your choice:\t').strip()
    while choice == '' or not choice.isdigit():
        print('invalid choice!! check again!!..\nEnter again!')       
        choice = input('1.name\n2.age\n3.address\n4.salary\nEnter your choice:\t').strip()
    
    name = input('Enter your name:\t').strip()
    while name == '' or not name.isalpha():
        print('Invalid! Check Again!')
        name = input('Enter your name:\t').strip()
          
    if choice == '1':
        new_name = input('Enter new name:\t').strip()
        while new_name == '' or not new_name.isalpha():
            print('Invalid! Check Again!')
            new_name = input('Enter new name:\t').strip()  
        
        for detail_p in update_people:
            if detail_p['name'] == name:
                detail_p['name'] = new_name
                break
    elif choice == '2':
        new_age = input('enter age:\t').strip()
        while new_age == '' or not new_age.isdigit():
            if int(new_age) <= 0:
                print('check Age!!\nTry Again!')
                new_age = input('Enter Age: \t').strip()
            else:
                for detail_p in update_people:
                    if detail_p['name'] == name:
                        detail_p['age'] = new_age
                        break
                return
    

details()
print('-'*40)

display()
print('-'*40)
search_people()
print('-'*40)
update_details()
print('-'*40)
display()
print('-'*40)