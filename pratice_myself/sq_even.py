#Create a list of squares of even numbers only between 1 and 50.
l = [i for i in range(1, 51)]
sq_even = [i**2 for i in l if i % 2 == 0]
print(sq_even)
