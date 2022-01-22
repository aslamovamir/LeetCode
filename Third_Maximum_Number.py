# Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.

 

# Example 1:

# Input: nums = [3,2,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2.
# The third distinct maximum is 1.
# Example 2:

# Input: nums = [1,2]
# Output: 2
# Explanation:
# The first distinct maximum is 2.
# The second distinct maximum is 1.
# The third distinct maximum does not exist, so the maximum (2) is returned instead.
# Example 3:

# Input: nums = [2,2,3,1]
# Output: 1
# Explanation:
# The first distinct maximum is 3.
# The second distinct maximum is 2 (both 2's are counted together since they have the same value).
# The third distinct maximum is 1.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # get all the distinct elements in a set
        set_nums = set(nums)
        # convert the set back to list
        nums = list(set_nums)
        # if the lenghtb of distinct numbers is less than 3
        # we just return the max of this list
        if len(nums) < 3:
            return max(nums)
        # otherwise, we first sort this list and return the 3rd largest from the back
        else:
            nums.sort()
            return nums[len(nums)-3]
        
        
