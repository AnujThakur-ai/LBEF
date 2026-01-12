#Write a Python program to shuffle and print a specified list.

from random import shuffle
#creat a list
food = ["cookies", "brownies", "cake", "ice cream", "chocolate"]
#shuffle the list
shuffle(food)
#print the shuffled list
print("Shuffled list:", food)