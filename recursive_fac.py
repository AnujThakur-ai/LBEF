# factorial via recursion
def fact(n):
    if n == 0 or n== 1:
        return 1
    else:
        return n * fact(n-1)
        
        
r = fact(int(input("Enter a number to find factorial: ")))
print("Factorial is:", r)  
    
