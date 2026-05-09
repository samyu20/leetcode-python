""" Problem:#9. Palindrome Number
Given an integer x, return True if x is a palindrome,
and False otherwise.
A palindrome number reads the same forward and backward.

Example:
Input : x = 121, Output: True
Input : x = -121 ,Output: False"""

# Algorithm:
# Negative numbers cannot be palindrome
# Store the original number
# Reverse the number using modulo and floor division
# Compare reversed number with original number
# Return True if both are equal, otherwise False

def is_palindrome_num(x):

    if x <0:                           # negative numbers are not palindrome
        return False

    reverse = 0                        # stores reversed number
    original = x                       # keep original value

    while x >0:
        digit = x %10                   # get last digit
        reverse = reverse *10 +digit    # build reversed number
        x=x//10                         # remove last digit

    return reverse == original          # compare original and reversed

print(is_palindrome_num(-121))

# Time Complexity  : O(log n) — traverses each digit once
# Space Complexity : O(1) — only variables are used