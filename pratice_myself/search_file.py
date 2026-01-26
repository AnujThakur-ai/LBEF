import os

if not os.path.exists('search.txt'):
    with open('search.txt', 'w') as file:
        file.write('Name                age\n')
        file.write('-------------------- ----\n')
    with open('search.txt', 'a') as file:
        file.write('anuj                20\n')
        file.write('shuv                21\n')

# Search functionality
search_name = input("Enter name to search: ")

with open('search.txt', 'r') as file:
    found = False
    print("\nSearch Results:")
    print("-" * 30)
    for line in file:
        if search_name.lower() in line.lower():
            # Parse the line to get all details
            parts = line.split()
            if len(parts) >= 2:
                name = parts[0]
                age = parts[1]
                print(f"Name: {name}")
                print(f"Age: {age}")
                print("-" * 30)
                found = True
    
    if not found:
        print(f"'{search_name}' not found in the file")

