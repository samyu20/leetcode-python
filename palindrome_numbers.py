#Given an integer x, return true if x is a palindrome, and false otherwise.
# Input: x = 121 , Output: true
#Input: x = -121 , Output: false

def is_palindrome_num(x):

    if x <0:
        return False
    reverse = 0
    original = x

    while x >0:
        digit = x %10
        reverse = reverse *10 +digit
        x=x//10
    return reverse == original

print(is_palindrome_num(-121))