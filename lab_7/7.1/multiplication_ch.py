# 7.      Write a Program for the following Requirement 
        
# 	Eg:
#   	 Input: a4b3c2 
#  	 Output: aaaabbbcc 
input_str = input("Enter the string: ")
char_result = ''
for char in input_str:
    if char.isalpha():
        char_result += char * int(input_str[input_str.index(char) + 1])
print("Resulting string:", char_result)