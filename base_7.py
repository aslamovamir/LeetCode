# Given an integer num, return a string of its base 7 representation.

 

# Example 1:

# Input: num = 100
# Output: "202"
# Example 2:

# Input: num = -7
# Output: "-10"

class Solution:
    def convertToBase7(self, num: int) -> str:
        answer = []
        negative = False
        if num < 0:
            negative = True
        elif num == 0:
            return "0"
        num = abs(num)
        while num != 0:
            answer.insert(0,str(num%7))
            num //= 7
        if negative:
            answer.insert(0, '-')
        return "".join(answer)
      
