import random
import string

def get_random_string(length):

    # ascii_lowercase	Contain all lowercase letters
    #     ascii_uppercase	Contain all uppercase letters
    # ascii_letters	Contain both lowercase and uppercase letters
    # digits	Contain digits ‘0123456789’.
    # punctuation	All special symbols !”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.
    # whitespace	Includes the characters space, tab, linefeed, return, formfeed, and vertical tab [^ \t\n\x0b\r\f]
    # printable	characters that are considered printable. This is a combination of constants digits, letters, punctuation, and whitespace.

    letters = string.printable
    result_str = ''.join(random.choice(letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

get_random_string(int(input('How many characters? ')))