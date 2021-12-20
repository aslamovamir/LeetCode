# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        Dict = {}
        for char in s:
            if char in Dict:
                Dict[char] += 1
            else:
                Dict [char] = 1
        
        for i in range(len(s)):
            if Dict[s[i]] == 1:
                return i
            
        return -1
