# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"

class Solution:
    def reverseVowels(self, s: str) -> str:
        # main strategy is to store all the vowels in the string in a stack
        # and then putting them back in reverse order
        Vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        Stack = []
        answer = ''
        
        # collect vowels in stack
        for char in s:
            if char in Vowels:
                Stack.append(char)
        
        # go through the string and if the char is a vowel, replace it with the 
        # vowel from the stack
        for i in range(len(s)):
            if s[i] in Vowels:
                answer += Stack.pop()
            else:
                answer += s[i]
                
        return answer
