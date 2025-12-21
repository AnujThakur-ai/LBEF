'''
AREA OF TRAPEZOID
1. height base1 and base 2
2 formula 0.5 * h(b1 + b2)
3. display the value

'''

height = eval(input('enter height : '))
b1 = eval(input('enter base 1 : '))
b2 = eval(input('enter base 2 : '))

#formula + display
print(f'Area of trapezoid {round(0.5 *height * (b1+b2), 2)}')
