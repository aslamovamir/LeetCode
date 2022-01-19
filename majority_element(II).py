# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: [3]
# Example 2:

# Input: nums = [1]
# Output: [1]
# Example 3:

# Input: nums = [1,2]
# Output: [1,2]


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        map_freq = {}
        
        # let's count the frequency of all the numbers first
        for num in nums:
            if num not in map_freq:
                map_freq[num] = 1
            else:
                map_freq[num] += 1
        
        # the boundary by which the frequency of the number should be greater or at
        boundary = len(nums)//3
        set_num = set()
        for num in nums:
            if map_freq[num] > boundary:
                set_num.add(num)
        
        return set_num
      
      
