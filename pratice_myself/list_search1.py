#to search the data from the list

l = []
while True:
    # Name input with validation
    name = input('Enter name:')
    if not name.isalpha():
        print('Please Enter string only')
        continue
    else:
        l.append(name)
    
    # Age input with validation
    while True:
        try:
            age = int(input('enter age: '))
            if 1 <= age <= 100:
                l.append(age)
                break
            else:
                print('Age must be between 1 and 100!')
        except ValueError:
            print('Invalid Age, please enter a number!')
    
    # Continue prompt with validation
    while True:
        try:
            ask = int(input('Do you want to continue or not(0 for no/ 1 for yes): \t'))
            if ask == 0 or ask == 1:
                break
            else:
                print('Invalid input! Please enter 0 or 1.')
        except ValueError:
            print('Invalid input! Please enter a number.')
    
    if ask == 0:
        break

#search 
d = {}
while True:
    try:
        
        search_Ask = int(input('Do you want to search or not ( 1 for yes/ 0 for no)'))
        if search_Ask == 0:
            break
        elif search_Ask == 1:
            w = input('enter the search item: \t')
            found = False
            for word in l:
                if w == word:
                    d[w.lower()] = d.get(w.lower(), 0) + 1
                    print(f'{w} found! Count: {d[w.lower()]}')
                    found = True
                    break
            if not found:
                print(f'{w} not found in the list!')
        else:
            print('Invalid input! please enter 0 or 1!')
    except ValueError:
        print('Invalid Input! please enter a number!')

