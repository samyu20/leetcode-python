""" Problem: #485. Max Consecutive Ones
Given a binary array nums, return the maximum number of consecutive 1's
in the array.

Example:
Input : nums = [1,1,0,1,1,1] , Output: 3"""

# Algorithm:
# Traverse through the array
# If the current element is 1, increase count
# If the current element is 0, reset count to 0
# Store the maximum consecutive count in max_count
# Return max_count

def FindMaxConsecutiveOnes(nums):

    count = 0                  # stores current consecutive 1's count
    max_count = 0              # stores maximum consecutive 1's
    for n in nums:
        if n == 0:             # reset count when 0 is found
            count = 0
        else:
            count += 1         # increase count for consecutive 1's
        if max_count < count:  # update maximum count
            max_count = count
    return max_count

nums = [1, 1, 0, 1, 1, 1]
print("Maximum Consecutive Ones:", FindMaxConsecutiveOnes(nums))

# Time Complexity  : O(n) — single traversal through the array
# Space Complexity : O(1) — only variables are used