# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "God Ding"
# Output: "doG gniD"
 

# Constraints:

# 1 <= s.length <= 5 * 104
# s contains printable ASCII characters.
# s does not contain any leading or trailing spaces.
# There is at least one word in s.
# All the words in s are separated by a single space.


class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ""
        # a list used to reverse the letters of a word in the string
        reverse_bucket = []
        
        for i in range(len(s)):
            # a white space will indicate the end of the word
            if s[i] == ' ':
                answer += "".join(reverse_bucket)
                answer += ' '
                reverse_bucket.clear()
                continue
            # if we reach the end of the string, we append the last word
            elif i == len(s)-1:
                reverse_bucket.insert(0, s[i])
                answer += "".join(reverse_bucket)
                break
            reverse_bucket.insert(0, s[i])
        
        return answer
      
      
