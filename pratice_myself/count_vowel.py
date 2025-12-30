def count_vowel(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonant(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def ignore_space(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string.")
    return s.replace(" ", "")

if __name__ == "__main__":
    #inpu
    string = input("Enter a string: ")
    print('Number of vowels: ', count_vowel(string))
    print('Number of consonants: ', count_consonant(string))
    print('String without spaces: ', ignore_space(string))