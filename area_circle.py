# area of circle
'''

1. ask for radius
2. use constant pie.
3. formula pie * r**2.
4. display result

'''

# code
radius = eval(input('enter radius : \t'))
# constant pie
PIE = 22/7
area_cir = PIE * radius ** 2
print(f'Area of circle having radius {radius} is {round(area_cir, 2)}')