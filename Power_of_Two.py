# Given an integer n, return true if it is a power of two. Otherwise, return false.

# An integer n is a power of two, if there exists an integer x such that n == 2x.

 

# Example 1:

# Input: n = 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: n = 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: n = 3
# Output: false
 

# Constraints:

# -231 <= n <= 231 - 1
 

# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # we know that if n is odd and is greater than 1, it is not a power of 2
        if n > 1 and n%2 != 0:
            return False
        
        # this will act as an iterator power index
        pow_index = 0
        while True:
            # if 2 to the power of the iterator is equal to n, than we know n is a power of 2
            if 2**pow_index == n:
                return True
            # if the result exceeded the value of n, we know it is not a power of 2
            elif 2**pow_index > n:
                return False
            # iterator the iterator index
            pow_index += 1
        
