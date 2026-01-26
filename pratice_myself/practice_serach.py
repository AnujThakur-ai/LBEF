
import os

if not os.path.exists('file_search.csv') :
    with open('file_search.csv', 'w') as file:
        file.write('Name, age \n')
    
    with open('file_search.csv', 'a') as file:
        file.write('anuj,20\n')
        file.write('shiv,21\n')
        
#search

search_d = input('Enter name to search:\\t')

with open('file_search.csv', 'r') as file:
    found = False
    for line in file:
        if search_d in line:
            print(line.strip())
            found = True
    
    if not found:
        print(f"'{search_d}' not found")
