'''result = []
for i in range(1, 21):
    if i % 3 == 0:
        result.append(i*i)'''
        


result = [ i * i for i in range(1, 21) if i % 3 == 0]
print(result)