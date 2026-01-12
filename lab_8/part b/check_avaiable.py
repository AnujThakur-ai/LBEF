# Write a Python code to create a list number using these number = 65, 75, 85, 95, 105 and check number that prompt the user to enter a number to check that number is available or not in list.

l = [65, 75, 85, 95, 105]
# prompt the user to enter a number
num = int(input('Enter a number to check in the list: '))

for i in l:
    if i == num: 
        print(f' The number {num} is available in the list at index {l.index(i)}')
        break
else:
    print(f'The number {num} is not available in the list')
        