#first fil
f = open('demo.txt', 'w')
f.write('hello, this is my first program.\n my name is Anuj kumar Thkaur.')
f.close()

fp = open('demo.txt', 'r')
print(fp.readline())
fp.close()
fp = open('demo.txt', 'r')
print(fp.readlines())
fp.close()

# with open('demo.txt', 'x') as ff:
#     ff.write('myself anuj.........')#FileExistsError: [Errno 17] File exists: 'demo.txt'
    
# with open('demooo.txt', 'x') as fff:
#     fff.write('myself')
# print('with mode x:')
with open('demooo.txt', 'r') as ffff:
    print(ffff.readlines())
    