# Given an integer n, return true if it is a power of three. Otherwise, return false.

# An integer n is a power of three, if there exists an integer x such that n == 3x.
# Example 1:

# Input: n = 27
# Output: true
# Example 2:

# Input: n = 0
# Output: false
# Example 3:

# Input: n = 9
# Output: true
# Example 4:

# Input: n = 45
# Output: false

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # if n is 0, we know it is not a power of 3
        if n == 0:
            return False
        # we continue looping through the quotients 
        # until it is 1
        while n != 1:
            # runner is the remainder 
            # if it is 0, we know the quotient is divisible by 3
            runner = int(n%3)
            if runner != 0:
                return False
            else:
                n = int(n/3)
                
        return True
