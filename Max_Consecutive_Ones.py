# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer = 0
        consequence = 0
        in_conseq = False
        for i in range(len(nums)):
            if nums[i] == 1:
                consequence += 1
                in_conseq = True
            elif nums[i] == 0:
                if in_conseq:
                    in_conseq = False
                    answer = max(answer, consequence)
                    consequence = 0
            if i == len(nums) - 1:
                    answer = max(answer, consequence)
        
        return answer
      
      
