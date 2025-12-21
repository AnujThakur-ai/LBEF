def perimeter(sides):
    return sum(sides)

print(perimeter(map(int, input('enter numbers : ').split())))

#for *args
'''
def perimeter(*sides):
    return sum(sides)

print(perimeter(*map(int, input('enter numbers : ').split())))'''
