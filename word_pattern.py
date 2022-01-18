# Given a pattern and a string s, find if s follows the same pattern.

# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

# Example 1:

# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:

# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:

# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # first, split the string s into a list of words
        words = s.split(" ")
        print(words)
        
        # if the lengths of the pattern and the words list is different
        # then there is no bijection
        if len(pattern) == len(words):
            # let's create 2 maps, that will map to each other
            word_to_letter = {}
            letter_to_word = {}
            
            for i in range(len(pattern)):
                # double check both on the letter and the corresponding word
                if pattern[i] not in letter_to_word:
                    if words[i] not in word_to_letter:
                        # both the letter and the corresponding word are not in the maps
                        # place them into the maps
                        letter_to_word[pattern[i]] = words[i]
                        word_to_letter[words[i]] = pattern[i]
                    else:
                        # at this point, the letter is not in letters map, but this word
                        # is in the words map, meaning, assigned to a different letter
                        return False
                else:
                    # the letter is in letters map
                    if words[i] in word_to_letter:
                        # word is also in the words map - check if they map to each other
                        if word_to_letter[words[i]] != pattern[i]:
                            return False
                    else:
                        # at this point, the letter maps to a different word
                        return False
            # at this point, everything maps to each other correspondingly       
            return True
        else:
            return False
          
          
