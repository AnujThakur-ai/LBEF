with open('seek_tell.txt', 'r') as file:
    data = file.read()
    print(data)
    
    #tell()
    print('1st postion of cursor:', file.tell())
    
    file.seek(0)
    print('2nd attempt t0 - ', file.tell())
    
    file.seek(50)
    print('3rd to 5- : ' , file.tell()
    )