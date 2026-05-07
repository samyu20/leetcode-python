#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target,
#assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

def TwoSum(nums,target):
    preMap = {}

    for i , n in enumerate(nums):
        differ = target - n

        if differ in preMap:
            return [i,preMap[differ]]

        preMap[n] = i
    return

nums = [2, 7, 11, 15]
target = 9
print(TwoSum(nums, target))