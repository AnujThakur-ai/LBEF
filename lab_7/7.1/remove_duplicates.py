r_set = set()
input_str = input("Enter the string: ")
for char in input_str:
    r_set.add(char)
unique_str = ''.join(r_set)
print("String after removing duplicates:", unique_str)