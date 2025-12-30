#function to count the min and max in a list
def mini(l: list):
    for i in l:
        if not isinstance(i, (int, float)):
            raise ValueError("All elements in the list must be integers or floats.")
    if len(l) == 0:
        raise ValueError("The list cannot be empty.")
    minimum = l[0]
    for num in l:
        if num < minimum:
            minimum = num
    return minimum

def maxi(l: list):
    for i in l:
        if not isinstance(i, (int, float)):
            raise ValueError("All elements in the list must be integers or floats.")
    if len(l) == 0:
        raise ValueError("The list cannot be empty.")
    maximum = l[0]
    for num in l:
        if num > maximum:
            maximum = num
    return maximum

if __name__ == "__main__":
    #take a list of integers or floats
    l = []
    #ask for user how many elements to be added in list
    n = int(input('How many elements you want to add in list: '))
    for num in range(n):
        element = eval(input('Enter element: '))
        l.append(element)
    
    print("Minimum value in the list is:", mini(l))
    print("Maximum value in the list is:", maxi(l))
