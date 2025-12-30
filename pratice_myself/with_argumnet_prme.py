# function with argument prime
def is_prime(num):
    if num > 1:
        for i in range(2, num//2 + 1):
            if (num % i == 0):
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        raise ValueError("Number should be greater than 1 to check for prime.")
    
if __name__ == "__main__":
    number = int(input('Enter number: '))
    is_prime(number)