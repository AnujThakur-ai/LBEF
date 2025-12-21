# take input
x, y = map(int, input('Enter two numbers: ').split())

if x < 1 or y < 1:
    print('Invalid input!!')
else:
    a, b = x, y  # copy originals for GCD calculation

    # GCD using subtraction method
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    gcd = a
    lcm = (x * y) // gcd  # use original numbers for LCM

    print("GCD:", gcd)
    print("LCM:", lcm)
