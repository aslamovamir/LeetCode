# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peaked = False
        went_up = False
        
        prev = arr[0]
        
        for i in range(1, len(arr)):
            if arr[i] == prev:
                return False
            if prev < arr[i]:
                if not went_up:
                    went_up = True
                elif went_up and peaked:
                    return False
                prev = arr[i]
            else:
                if not went_up:
                    return False
                else:
                    if not peaked:
                        peaked = True
                    prev = arr[i]
                            
        if not peaked:
            return False
        else:
            return True
          
          
