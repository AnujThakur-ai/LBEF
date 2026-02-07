# aternate chars merge
# #	Eg: 
#          Input: Ravi and Teja
#          Output: RTaevjia

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = ""
i = 0
while i < len(str1) or i < len(str2):
    if i < len(str1):
        result += str1[i]
    if i < len(str2):
        result += str2[i]
    i += 1
print("Alternate merge of the two strings is:", result)