# An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is any substring of the 
# string "abcdefghijklmnopqrstuvwxyz".

# For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
# Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.

 

# Example 1:

# Input: s = "abacaba"
# Output: 2
# Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
# "ab" is the longest continuous substring.
# Example 2:

# Input: s = "abcde"
# Output: 5
# Explanation: "abcde" is the longest continuous substring.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of only English lowercase letters.

class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest = 0
        
        in_sequence = False
        distance = 1
        for i in range(len(s)):
            if i + 1 < len(s):
                if ord(s[i+1]) - ord(s[i]) == 1:
                    if in_sequence:
                        distance += 1
                    else:
                        in_sequence = True
                        distance += 1
                else:
                    if in_sequence:
                        in_sequence = False
                        longest = max(longest, distance)
                        distance = 1
                    else:
                        continue
            if i + 1 == len(s):
                longest = max(longest, distance)
        
        return longest
      
