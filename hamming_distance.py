# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, return the Hamming distance between them.

 

# Example 1:

# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
#        ↑   ↑
# The above arrows point to positions where the corresponding bits are different.
# Example 2:

# Input: x = 3, y = 1
# Output: 1
 

# Constraints:

# 0 <= x, y <= 231 - 1

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        answer = 0
        bigger = x if x > y else y
        smaller = x if y == bigger else y
        
        stop = False
        while True:
            if bigger%2 != smaller%2:
                answer += 1
            bigger //= 2
            smaller //= 2
            if smaller == 0:
                while True:
                    if bigger%2 == 1:
                        answer += 1
                    bigger //= 2
                    if bigger == 0:
                        stop = True
                        break
            if stop:
                break
        
        return answer
      
      
