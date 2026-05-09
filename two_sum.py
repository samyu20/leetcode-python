"""Problem:#1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.
Assume that each input has exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

Example:
Input : nums = [2,7,11,15], target = 9, Output: [0,1]"""

# Algorithm:
# Create a hashmap to store visited numbers
# Traverse through the array using enumerate
# Find the difference between target and current number
# Check if difference already exists in hashmap
# If found, return current index and stored index
# Otherwise store current number and index in hashmap

def TwoSum(nums,target):

    preMap = {}                         # stores value:index
    for i , n in enumerate(nums):
        differ = target - n            # required number to reach target
        if differ in preMap:           # check if complement exists
            return [i,preMap[differ]]
        preMap[n] = i                  # store current number and index
    return
nums = [2, 7, 11, 15]
target = 9
print(TwoSum(nums, target))

# Time Complexity  : O(n) — single traversal through the array
# Space Complexity : O(n) — hashmap stores array elements