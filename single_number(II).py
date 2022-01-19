# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element 
# and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # let's store all the numbers and thier frequencies in the list
        # in a dictionary
        map_freq = {}
        
        for num in nums:
            if num not in map_freq:
                map_freq[num] = 1
            else:
                map_freq[num] += 1
        
        # now loop through the list and return the num with frequency 1
        for num in nums:
            if map_freq[num] == 1:
                return num
              
              
