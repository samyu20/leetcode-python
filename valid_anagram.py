"""Problem:#242. Valid Anagram
Given two strings s and t, return True if t is an anagram of s,
and False otherwise.
An anagram is formed by rearranging the letters of another word
using all the original characters exactly once.

Example:
Input : s = "anagram", t = "nagaram"
Output: True"""

# Algorithm:
# Check whether both strings have equal length
# Create a dictionary to store character counts
# Count each character from string s
# Traverse string t and decrease character counts
# If a character is missing or count becomes negative, return False
# Otherwise return True

def is_anagram(s,t):

    if len(s) != len(t):                         #length of the characters should be same
        return False
    count = {}                                   #empty dictionary
    for char in s:                               #count characters from s
        count[char] = count.get(char,0) + 1
    for char in t:                               #remove characters using t
        if char not in count:                    #character not found
            return False
        count[char] -=1                          #decrease character count
        if count[char] < 0:                      #extra character found
            return False
    return True
print(is_anagram("anagram", "nagaram"))

# Time Complexity  : O(n) — traverses both strings once
# Space Complexity : O(1) — fixed character storage (assuming lowercase letters)
