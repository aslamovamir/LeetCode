# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated 
# into n + 1 groups by n dashes. You are also given an integer k.

# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter 
# than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert 
# all lowercase letters to uppercase.

# Return the reformatted license key.

 

# Example 1:

# Input: s = "5F3Z-2e-9-w", k = 4
# Output: "5F3Z-2E9W"
# Explanation: The string s has been split into two parts, each part has 4 characters.
# Note that the two extra dashes are not needed and can be removed.
# Example 2:

# Input: s = "2-5g-3-J", k = 2
# Output: "2-5G-3J"
# Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
 

# Constraints:

# 1 <= s.length <= 105
# s consists of English letters, digits, and dashes '-'.
# 1 <= k <= 104

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        answer = ""
        size = 0
        met_first_dash = False
        # we will start grouping from the end, as the first group we know can have 
        # chars fewer than k
        # idea is to reverse s and start processing
        # after we get the processed string, we reverse it back, so we get the original standing of
        # the chars
        s = ''.join(reversed(s))
        
        for i in range(len(s)):
            if s[i] == '-':
                # we met a dash
                if size != k:
                    continue
                else:
                    # if the size of the group we have collected so far is equal to k,
                    # we reset the size and add the dash to the string answer
                    answer += '-'
                    size = 0
            else:
                # we met a char
                if size == k:
                    # if the size of the group we have been collecting is equal to k, we do a reset
                    answer += '-'
                    # if the char is a letter, we turn it upper-case
                    answer += (s[i] if s[i].isdigit() else s[i].upper())
                    size = 1
                else:
                    # we do a regular concatination of the char to the string answer
                    # if the char is a letter, we turn it upper-case
                    answer += (s[i] if s[i].isdigit() else s[i].upper())
                    size += 1
        
        # reverse the processed string back to orginal standing of the chars
        answer = ''.join(reversed(answer))
        # if the size of the string is 0, it means we did not get any chars
        if answer == '':
            return answer
        # if the first char is a dash, we know the first group did not have enough chars
        # so, we just get rid of the dash
        if answer[0] == '-':
            answer = answer[1:]
            
        return answer
      
      
