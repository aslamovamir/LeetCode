# You are given a 0-indexed integer array nums. You are also given an integer key, which is present in nums.

# For every unique integer target in nums, count the number of times target immediately follows an occurrence of key in nums. 
# In other words, count the number of indices i such that:

# 0 <= i <= nums.length - 2,
# nums[i] == key and,
# nums[i + 1] == target.
# Return the target with the maximum count. The test cases will be generated such that the target with maximum count is unique.

 

# Example 1:

# Input: nums = [1,100,200,1,100], key = 1
# Output: 100
# Explanation: For target = 100, there are 2 occurrences at indices 1 and 4 which follow an occurrence of key.
# No other integers follow an occurrence of key, so we return 100.
# Example 2:

# Input: nums = [2,2,2,2,3], key = 2
# Output: 2
# Explanation: For target = 2, there are 3 occurrences at indices 1, 2, and 3 which follow an occurrence of key.
# For target = 3, there is only one occurrence at index 4 which follows an occurrence of key.
# target = 2 has the maximum number of occurrences following an occurrence of key, so we return 2.
 

# Constraints:

# 2 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# The test cases will be generated such that the answer is unique.


class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        # we will collect the frequency of each value in a dictionary
        map_target = {}
        # this will help with determining the max frequency of all vals following the key
        max_freq = 0
        # this will keep updating and will eventually be equal to the val with max frequency
        max_target = nums[0]
        
        # go through the list
        for i in range(len(nums)):
            # if the value is the key and the next item is existent
            if nums[i] == key and i != len(nums)-1:
                # get its frequency in the map and see if it is greater in frequency than 
                # the others before
                if nums[i+1] not in map_target:
                    map_target[nums[i+1]] = 1
                    if max_freq < 1:
                        max_freq = 1
                        max_target = nums[i+1]
                else:
                    map_target[nums[i+1]] += 1
                    if map_target[nums[i+1]] > max_freq:
                        max_freq = map_target[nums[i+1]]
                        max_target = nums[i+1]
        
        # return the target with max frequency
        return max_target
      
      
