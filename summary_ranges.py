# You are given a sorted unique integer array nums.

# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by 
# exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"
# Example 2:

# Input: nums = [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: The ranges are:
# [0,0] --> "0"
# [2,4] --> "2->4"
# [6,6] --> "6"
# [8,9] --> "8->9"

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if len(nums) == 1:
            answer.append(str(nums[0]))
            return answer
        
        # let's loop through the numbers and check the difference betwen each pair
        # if the difference is 1, they form a sequence
        
        in_sequence = False
        for i in range(1, len(nums)):
            if not in_sequence:
                start_point = nums[i-1]
            if nums[i] - nums[i-1] == 1:
                if i == len(nums) - 1:
                    duration = f"{start_point}->{nums[i]}"
                    answer.append(duration)
                in_sequence = True
            else:
                if in_sequence:
                    end_point = nums[i-1]
                    duration = f"{start_point}->{end_point}"
                    answer.append(duration)
                    if i == len(nums) - 1:
                        answer.append(str(nums[i]))
                    in_sequence = False
                else:
                    answer.append(str(nums[i-1]))
                    if i == len(nums) - 1:
                        answer.append(str(nums[i]))
            
        return answer
                    
        
