# Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, 
# no letter appears in a single substring more than once.

# Return the minimum number of substrings in such a partition.

# Note that each character should belong to exactly one substring in a partition.

 

# Example 1:

# Input: s = "abacaba"
# Output: 4
# Explanation:
# Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
# It can be shown that 4 is the minimum number of substrings needed.
# Example 2:

# Input: s = "ssssss"
# Output: 6
# Explanation:
# The only valid partition is ("s","s","s","s","s","s").

class Solution:
    def partitionString(self, s: str) -> int:
        iterFreqSet = set()
        count = 0
        for i in range(len(s)):
            if s[i] not in iterFreqSet:
                iterFreqSet.add(s[i])
            else:
                count += 1
                iterFreqSet.clear()
                iterFreqSet.add(s[i])
            if i == len(s) - 1:
                if len(iterFreqSet) != 0:
                    count += 1
        
        return count
      