# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
# Example 2:

# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
# Example 3:

# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
# Example 4:

# Input: nums = [0]
# Output: 1
# Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort the list
        nums.sort()
        # get hold of the length of the list
        length = len(nums)
        # create an iterator variable to be incremented until it is equal to 'length' variable above
        iterator = 0
        # loop through the list while incrementing the iterator variable
        # if the iterator variable differes from any number in the now sorted list
        # return it
        for num in nums:
            if num != iterator:
                return iterator
            iterator += 1
            
        # check if the iterator is still not equal to the length of the list
        # if so return the iterator, because we can assume it is now eqaul to the 
        # length variable because of the increment operatioon at the for loop above
        return iterator
