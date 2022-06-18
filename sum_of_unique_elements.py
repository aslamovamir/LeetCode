# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.

 

# Example 1:

# Input: nums = [1,2,3,2]
# Output: 4
# Explanation: The unique elements are [1,3], and the sum is 4.
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: 0
# Explanation: There are no unique elements, and the sum is 0.
# Example 3:

# Input: nums = [1,2,3,4,5]
# Output: 15
# Explanation: The unique elements are [1,2,3,4,5], and the sum is 15.


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        # Dictionary solution
        Dict = dict()
        for num in nums:
            if num not in Dict:
                Dict[num] = 1
            else:
                Dict[num] += 1
        answer = 0
        for key,value in Dict.items():
            if value == 1:
                answer += key
        
        return answer
        
        # Set Solution
        Set = set()
        Set2 = set()
        
        for num in nums:
            if num in Set:
                Set.remove(num)
                Set2.add(num)
            else:
                if num not in Set2:
                    Set.add(num)
                        
        return sum(Set)
      
      
