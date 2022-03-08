# You are given a 0-indexed array of distinct integers nums.

# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum 
# respectively. Your goal is to remove both these elements from the array.

# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

 

# Example 1:

# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation: 
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number possible.
# Example 2:

# Input: nums = [0,-4,19,1,8,-2,-3,5]
# Output: 3
# Explanation: 
# The minimum element in the array is nums[1], which is -4.
# The maximum element in the array is nums[2], which is 19.
# We can remove both the minimum and maximum by removing 3 elements from the front.
# This results in only 3 deletions, which is the minimum number possible.
# Example 3:

# Input: nums = [101]
# Output: 1
# Explanation:  
# There is only one element in the array, which makes it both the minimum and maximum element.
# We can remove it with 1 deletion.
 

# Constraints:

# 1 <= nums.length <= 105
# -105 <= nums[i] <= 105
# The integers in nums are distinct.

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))
        
        # these booleans will helps us find if the min and max elements 
        # are relatively at the start of the list or at the end
        min_start = False
        max_start = False
        
        answer = 0
        # first deal with the min
        # find the realtive location in the list
        
        # if it is right at the center of the list, we will see if the max is relatively 
        # at the start or the end of the list - the idea is: it is less elements to delete if
        # both are at relatively the same side: either start or end
        if min_index == len(nums)//2:
            if max_index < len(nums)//2:
                answer += (min_index + 1)
                min_start = True
            else:
                answer += (len(nums) - min_index)
        elif min_index < len(nums)//2:
            answer += (min_index + 1)
            min_start = True
        else:
            answer += (len(nums) - min_index)
            
        # here too, if at the center, we see if the min is in the start or the end
        if max_index == len(nums)//2:
            if min_start:
                max_start = True
                if min_index < max_index:
                    answer += abs(max_index - min_index)
            else:
                max_start = True
                if min_index > max_index:
                    answer += abs(max_index - min_index)
        elif max_index < len(nums)//2:
            if min_start:
                if min_index < max_index:
                    answer += abs(max_index - min_index)
            else:
                answer += (max_index + 1)
            max_start = True
        else:
            if not min_start:
                if min_index > max_index:
                    answer += (abs(min_index - max_index))
            else:
                answer += (len(nums) - max_index)
        
        # we make the last check to see if fewer elements can be deleted from the 
        # opposite side from the side calculated above
        if min_start and not max_start:
            if max_index > min_index:
                if answer > max_index:
                    answer = max_index + 1
            else:
                if answer > min_index:
                    answer = min_index + 1
        elif not min_start and max_start:
            if min_index > max_index:
                if answer > min_index:
                    answer = min_index + 1
            else:
                if answer > max_index:
                    answer += max_index + 1
                          
            if (len(nums) - max_index) < answer:
                answer = len(nums) - max_index
                          
        
        return answer
        
        
