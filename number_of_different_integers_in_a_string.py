# You are given a string word that consists of digits and lowercase English letters.

# You will replace every non-digit character with a space. For example, "a123bc34d8ef34" will become " 123  34 8  34".
# Notice that you are left with some integers that are separated by at least one space: "123", "34", "8", and "34".

# Return the number of different integers after performing the replacement operations on word.

# Two integers are considered different if their decimal representations without any leading zeros are different.

 

# Example 1:

# Input: word = "a123bc34d8ef34"
# Output: 3
# Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.
# Example 2:

# Input: word = "leet1234code234"
# Output: 2
# Example 3:

# Input: word = "a1b01c001"
# Output: 1
# Explanation: The three integers "1", "01", and "001" all represent the same integer because
# the leading zeros are ignored when comparing their decimal values.

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        Set = set()
        collector = ""
        appending_num = False
        for ch in word:
            if ch.isdigit():
                appending_num = True
                collector += ch
            else:
                if appending_num:
                    appending_num = False
                    Set.add(int(collector))
                    collector = ""
        
        if appending_num:
            Set.add(int(collector))
        return len(Set)
      
