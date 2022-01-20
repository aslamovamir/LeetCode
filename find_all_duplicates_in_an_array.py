# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice,
# return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

 

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        Range = {}
        # put all the numbers in the range in a frequency dictionary 
        # that will initialize the frequency of each number
        for i in range(1, len(nums) + 1):
            Range[i] = 2
            
        answer = []
        # now check which numbers have frequency 2
        for i in range(len(nums)):
            if Range[nums[i]] == 1:
                answer.append(nums[i])
            else:
                Range[nums[i]] -= 1
        
        return answer
      
      
