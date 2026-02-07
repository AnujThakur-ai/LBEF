# 6.	Write a Program to Sort the Characters of the String with the First Alphabet Symbols followed by Numeric Values
 	
# 	Eg:
#   	 Input: B4A1D3 
#   	 Output: ABD134 
input_str = input("Enter the string: ")
alphabets = ''
numbers = ''
for char in input_str:
    if char.isalpha():
        alphabets += char
    elif char.isdigit():
        numbers += char
sorted_str = ''.join(sorted(alphabets)) + ''.join(sorted(numbers))
print("Sorted string:", sorted_str)