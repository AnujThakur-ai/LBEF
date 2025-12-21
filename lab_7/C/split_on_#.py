'''Write a Python program to split a given string on hash symbol and display each substring.
a. Given string = "Magic#Mirror#on#the#wall,#who#is#the#fairest#one#of#all?'''


#code

words = "Magic#Mirror#on#the#wall,#who#is#the#fairest#one#of#all?"

splited = words.split('#')

for word in splited:
    print(word)
    
