# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily 
# different) and swap the characters at these indices.

# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, 
# return false.

 

# Example 1:

# Input: s1 = "bank", s2 = "kanb"
# Output: true
# Explanation: For example, swap the first character with the last character of s2 to make "bank".
# Example 2:

# Input: s1 = "attack", s2 = "defend"
# Output: false
# Explanation: It is impossible to make them equal with one string swap.
# Example 3:

# Input: s1 = "kelb", s2 = "kelb"
# Output: true
# Explanation: The two strings are already equal, so no string swap operation is required.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # let's sum the total number of misplaced letters are in s1
        total_misplace = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                # check if the letter from s1 is in s2
                if s1[i] in s2:
                    total_misplace += 1
                else:
                    return False
        # if total misplaced letters are 2, we know we need 1 swap
        # if it is 0, we know we do not need any swaps
        if total_misplace == 2 or total_misplace == 0:
            return True
        else:
            return False
        
        
