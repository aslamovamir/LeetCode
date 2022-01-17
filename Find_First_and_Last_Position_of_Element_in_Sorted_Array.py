# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # let's first check if intially there is 1 number
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
        
        # let's store the positions in a list
        positions = []
        
        # let's go with the binary search algorithm
        mid = len(nums)//2
        left = 0
        right = len(nums)-1
        
        while left <= right:
            if nums[mid] < target:
                # update the left pointer
                left = mid + 1
                # update the mid pointer
                mid = (left + right)//2
                # if the mid pointer is at the start or end of the list
                # we know, we did not find the target so far
                if mid == 0 or mid == len(nums)-1:
                    if nums[mid] != target:
                        break
                    else:
                        positions.append(mid)
            elif nums[mid] > target:
                # update the right pointer
                right = mid - 1
                # update the mid pointer
                mid = (left + right)//2
                # if the mid pointer is at the start or end of the list
                # we know, we did not find the target so far
                if mid == 0 or mid == len(nums)-1:
                    if nums[mid] != target:
                        break
                    else:
                        positions.append(mid)
            else:
                # first append the mid pointer
                positions.append(mid)
                # now we check if near the mid pointer the numbers are equal to target
                if mid-1 >= 0:
                    # check one less the mid pointer
                    if nums[mid-1] == target:
                        positions.append(mid-1)
                        # iterator variable will help in looping trhough the numbers equal to target
                        iterate = mid-2
                        while iterate >= 0:
                            if target == nums[iterate]:
                                positions.append(iterate)
                                iterate -= 1
                            else:
                                break
                if mid+1 < len(nums):
                    # check one more the mid pointer
                    if nums[mid+1] == target:
                        positions.append(mid+1)
                        # iterator variable will help in looping trhough the numbers equal to target
                        iterate = mid+2
                        while iterate < len(nums):
                            if target == nums[iterate]:
                                positions.append(iterate)
                                iterate += 1
                            else:
                                break
                else:
                    break
                # we can break from the loop as at this point we found all the 
                # indeces at which the numbers in the list are equal to target
                break
        
        
        # let's create a helper function to filter the positions list
        def filter_pos(positions):
            if not positions:
                return [-1,-1]
            elif len(positions) == 1:
                positions.append(positions[0])
                return positions
            elif len(positions) == 2:
                positions.sort()
                return positions
            else:
                positions.sort()
                new_pos = []
                new_pos.append(positions[0])
                new_pos.append(positions[len(positions)-1])
                return new_pos
                    
        
        result = filter_pos(positions)
        
        return result
      
      
