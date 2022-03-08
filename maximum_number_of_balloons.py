# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        target = "balloon"
        target_map = {}
        for ch in target:
            if ch in target_map:
                target_map[ch] += 1
            else:
                target_map[ch] = 1
        
        text_map = {}
        for ch in text:
            if ch in text_map:
                text_map[ch] += 1
            else:
                text_map[ch] = 1
        
        counter = 0
        finish = False
        while True:
            for key, value in target_map.items():
                if key in text_map:
                    if text_map[key] - value < 0:
                        finish = True
                        break
                    else:
                        text_map[key] -= value
                else:
                    finish = True
                    break
            
            if finish:
                break
            else:
                counter += 1
        
        return counter
      
      
