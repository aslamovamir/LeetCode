# There is a malfunctioning keyboard where some letter keys do not work. All other keys on the keyboard work properly.

# Given a string text of words separated by a single space (no leading or trailing spaces) and a string brokenLetters 
# of all distinct letter keys that are broken, return the number of words in text you can fully type using this keyboard.

 

# Example 1:

# Input: text = "hello world", brokenLetters = "ad"
# Output: 1
# Explanation: We cannot type "world" because the 'd' key is broken.
# Example 2:

# Input: text = "leet code", brokenLetters = "lt"
# Output: 1
# Explanation: We cannot type "leet" because the 'l' and 't' keys are broken.
# Example 3:

# Input: text = "leet code", brokenLetters = "e"
# Output: 0
# Explanation: We cannot type either word because the 'e' key is broken.
 

# Constraints:

# 1 <= text.length <= 104
# 0 <= brokenLetters.length <= 26
# text consists of words separated by a single space without any leading or trailing spaces.
# Each word only consists of lowercase English letters.
# brokenLetters consists of distinct lowercase English letters.

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        # seperate the broken letters into a list of letters
        broken = list(brokenLetters)
        # seperate the words in text into a list of words
        words = text.split(' ')
        
        # now go through each word and see if it contains any one of the broken letters
        # if not, increment the counter
        counter = 0
        count = True
        for word in words:
            for broken_letter in broken:
                if broken_letter in word:
                    # we do not count this word
                    count = False
                    break
            # if we count this word, increment the counter
            if count:
                counter += 1
            # if not, reset the count
            else:
                count = True
        
        return counter
      
