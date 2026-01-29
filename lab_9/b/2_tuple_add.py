# #. You were given a tuple named turtle = (1, “Hello”). Write a python program to 
# a. Add on item 5 using + 
# b. Add on item “single” using append (). 

# tuple
turtle = (1, 'Hello')


print(turtle + (5,))
turtle = list(turtle)
turtle.append('single')
print(tuple(turtle))