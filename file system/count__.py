with open ('lbef.txt', 'w') as fp:
    fp.write('Lord buddha education foundation was established in 1998AD. \nIt is the first IT collage of nepal.\n about 15000+ alumuni are already have completed their bachelor level education from this prestigious collage\nHappy to be the part if the collage.')
    
with open('lbef.txt', 'r') as fp:
    r = fp.read()
    char_count = 0
    r.strip()
    for ch in r:
        char_count +=1
    
    print('character count: ', char_count)    
    
with open ('lbef.txt', 'r') as fp:
    record = fp.read()
    space_count = 0
    
    word_count = 0
    
    print('record:')
    print(record )
    
    #space count
    for space in record:
        if space == ' ':
            space_count +=1

    print(
        'space count: ',space_count
    )
    