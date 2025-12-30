def process(s:str):
    print("Original String: ", s)
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    #case insensitive comparison
    s = s.lower()
    #remove spaces for palindrome check
    s = s.replace(" ", "")
    print("case insensitive: ", s)
    #check if palindrome
    is_palindrome = s == s[::-1]
    print('Is Palindrome: ', is_palindrome)
    
if __name__ == "__main__":
    string = input("Enter a string: ")
    process(string)
    