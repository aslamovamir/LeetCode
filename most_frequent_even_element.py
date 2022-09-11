# Given an integer array nums, return the most frequent even element.

# If there is a tie, return the smallest one. If there is no such element, return -1.

 

# Example 1:

# Input: nums = [0,1,2,2,4,4,1]
# Output: 2
# Explanation:
# The even elements are 0, 2, and 4. Of these, 2 and 4 appear the most.
# We return the smallest one, which is 2.
# Example 2:

# Input: nums = [4,4,4,9,2,4]
# Output: 4
# Explanation: 4 is the even element appears the most.
# Example 3:

# Input: nums = [29,47,21,41,13,37,25,7]
# Output: -1
# Explanation: There is no even element.

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        tracker = {}
        most = 0
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                if nums[i] not in tracker:
                    tracker[nums[i]] = 1
                    if 1 > most:
                        most = 1
                else:
                    tracker[nums[i]] += 1
                    if tracker[nums[i]] > most:
                        most = tracker[nums[i]]
    
        list_ties = []
        for k, v in tracker.items():
            if v == most:
                list_ties.append(k)
        
        if len(list_ties) == 0:
            return -1
        list_ties.sort()
        
        return list_ties[0]
        
        
