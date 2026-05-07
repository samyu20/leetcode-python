#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Input: s = "anagram", t = "nagaram" ,Output: true
# Input: s = "rat", t = "car" ,Output: false

def is_anagram(s,t):

    if len(s) != len(t):                         #length of the charcter should be same else it will be false
        return False
    count = {}                                   #empty dictionary

    for char in s:                                #count charcters from s
        count[char] = count.get (char,0) + 1

    for char in t:                                #removing charcters from t
        if char not in count:                     #if the charcters from 't' not in count , it will be false
            return False

        count[char] -=1                           #removing each charchter from count for balancing

        if count[char] < 0:                       #any count became negative , it will be false
            return False

    return True

print(is_anagram("anagram", "nagaram"))
