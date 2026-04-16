#Given a binary array nums, return the maximum number of consecutive 1's in the array.
#Input: nums = [1,1,0,1,1,1] , Output: 3

def FindMaxConsecutiveOnes(nums):
    count = 0                  #1 ,2 ,0,1,2,3
    max_count = 0              #0 ,1, 2,2,2,3

    for n in nums:
        if n == 0:
            count = 0
        else:
            count += 1

        if max_count < count:   #t,t,f,f,f,t
            max_count = count

    return max_count

nums = [1, 1, 0, 1, 1, 1]
print("Maxium Consecutive Ones:", (FindMaxConsecutiveOnes(nums)))