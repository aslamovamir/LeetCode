# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
# of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence 
# of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false
 

# Constraints:

# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    return False
        last_found_at = -1
        found = False
        greedy = False
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    if j < last_found_at:
                        greedy = True
                        continue
                    elif j == last_found_at:
                        continue
                    else:
                        found = True
                        last_found_at = j
                        break
            if greedy:
                if not found:
                    return False
            if found:
                found = False
            else:
                return False
        
        return True
      
