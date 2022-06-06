# You are given a 0-indexed array nums that consists of n distinct positive integers. Apply m operations to this array,
# where in the ith operation you replace the number operations[i][0] with operations[i][1].

# It is guaranteed that in the ith operation:

# operations[i][0] exists in nums.
# operations[i][1] does not exist in nums.
# Return the array obtained after applying all the operations.

 

# Example 1:

# Input: nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]]
# Output: [3,2,7,1]
# Explanation: We perform the following operations on nums:
# - Replace the number 1 with 3. nums becomes [3,2,4,6].
# - Replace the number 4 with 7. nums becomes [3,2,7,6].
# - Replace the number 6 with 1. nums becomes [3,2,7,1].
# We return the final array [3,2,7,1].
# Example 2:

# Input: nums = [1,2], operations = [[1,3],[2,1],[3,2]]
# Output: [2,1]
# Explanation: We perform the following operations to nums:
# - Replace the number 1 with 3. nums becomes [3,2].
# - Replace the number 2 with 1. nums becomes [3,1].
# - Replace the number 3 with 2. nums becomes [2,1].
# We return the array [2,1].

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        # make a map of all the nums, with indeces as values
        map_nums = {}
        for i in range(len(nums)):
            map_nums[nums[i]] = i
        
        # loop through the changes, apply changes abd update the map
        for pair in operations:
            if pair[0] in map_nums:
                nums[map_nums[pair[0]]] = pair[1]
                index = map_nums[pair[0]]
                del map_nums[pair[0]]
                map_nums[pair[1]] = index
            
        return nums
      
