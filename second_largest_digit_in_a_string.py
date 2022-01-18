# Given an alphanumeric string s, return the second largest numerical digit that appears in s, or -1 if it does not exist.

# An alphanumeric string is a string consisting of lowercase English letters and digits.

 

# Example 1:

# Input: s = "dfa12321afd"
# Output: 2
# Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.
# Example 2:

# Input: s = "abc1111"
# Output: -1
# Explanation: The digits that appear in s are [1]. There is no second largest digit. 

class Solution:
    def secondHighest(self, s: str) -> int:
        # let's first store all the digits in a seperate list
        digits = []
        
        for char in s:
            if char.isdigit():
                # store the digit in int type
                digits.append(int(char))
        
        # if we did not find any digits
        if len(digits) == 0:
            return -1
        # determine the max element and remove all instances of it from the list
        max_element = max(digits)
        while max_element in digits:
            digits.remove(max_element)
        # if we are not left with any digits
        if len(digits) == 0:
            return -1
        else:
            return max(digits)
          
