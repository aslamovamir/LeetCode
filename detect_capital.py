# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_start = False
        more_cap = False
        non_cap = False
        
        for i in range(len(word)):
            if i == 0 and word[i].isupper():
                cap_start = True
            else:
                if word[i].isupper():
                    if cap_start:
                        more_cap = True
                    else:
                        return False
                else:
                    if cap_start and more_cap:
                        # we know that we both found a cap at the start and somewhere else
                        return False
                    else:
                        non_cap = True
        
        if more_cap and non_cap:
            return False
        return True
                    
