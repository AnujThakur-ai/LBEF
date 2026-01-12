    # 3. 
    # 4. Write a Python program to get the difference between the two lists.
    
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

diff_list = list(set(list1) - set(list2))
print("Difference between the two lists:", diff_list)