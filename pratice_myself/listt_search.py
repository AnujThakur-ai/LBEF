l = [['anuj', 'kumar', 20], ['shib', 'kuamr', 20]]
found = False

for person in l:
    if 'anuj' in person:
        print(f'Found anuj with all details: {person}')
        found = True

if not found:
    print('anuj not found in the list')
        