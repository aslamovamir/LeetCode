# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        product_total = 1
        zero_at = index
        met_zero = False
        met_nonzero = False
        met_zero_mult = False
        
        for num in nums:
            if num == 0:
                if met_zero:
                    met_zero_mult = True
                met_zero = True
                continue
            product_total *= num
            met_nonzero = True
            
        if not met_nonzero:
            product_total = 0
        if met_zero_mult:
            for num in nums:
                answer.append(0)
                
            return answer
        
        for num in nums:
            if num == 0 and met_zero:
                answer.append(product_total)
            else:
                if met_zero:
                    answer.append(0)
                else:
                    answer.append(product_total//num)
        
        return answer
      
