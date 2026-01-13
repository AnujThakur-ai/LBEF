#write program to print the details of any student and name, age, email, stored inside the dictionary

# d = {
#     'name': ['anuj', 'sabina', 'samira'],
#     'age' : [19, 2, 1],
#     'email': ['anuj123@gmail.com', 'sabina123@gmail.com', 'samira123@gmail.com']
    
# }
# print('using for loop: ')
# for k, v in d.items():
#     print(k , v)



users = []

n = int(input("How many users? "))

for i in range(n):
    d = {}
    d['name'] = input('Enter name: ')
    d['age'] = int(input('Enter age: '))
    d['email'] = input('Enter email: ')
    print('--' * 30)
    users.append(d)

print(users)
