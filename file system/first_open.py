with open('file.txt', 'w') as fp:
    fp.write('My name is Anuj Kumar Thakur.\n This is a another method to open via python.')
    
with open('file.txt', 'r') as fp:
    print(fp.read())
    