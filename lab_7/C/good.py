str = "i'm a good boy/girl but my parents always scold me"
count = len(str)
new_str = str[:20]
str_replace = str.replace('parents', 'lecturers')
str1 = ' I pretend to be good, HAHAHA'
str_conc = str + str1

for i in range(len(str)):
    if str[i] == 'good':
        str[i] = str[i].upper()
print(str)

