# A sentence is a string of single-space separated words where each word consists only of lowercase letters.

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

# Example 1:

# Input: s1 = "this apple is sweet", s2 = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: s1 = "apple apple", s2 = "banana"
# Output: ["banana"]
 

# Constraints:

# 1 <= s1.length, s2.length <= 200
# s1 and s2 consist of lowercase English letters and spaces.
# s1 and s2 do not have leading or trailing spaces.
# All the words in s1 and s2 are separated by a single space.


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        # first, break the strings into a list of words
        list1 = s1.split(" ")
        list2 = s2.split(" ")
        
        # now we will collect the frequencies of each word in both lists in a map
        map_words = {}
        
        for word in list1:
            if word not in map_words:
                map_words[word] = 1
            else:
                map_words[word] += 1
        
        for word in list2:
            if word not in map_words:
                map_words[word] = 1
            else:
                map_words[word] += 1
        
        # now we collect all the words with frequency 1 in a list
        answer = []
        
        for word, freq in map_words.items():
            if freq == 1:
                answer.append(word)
        
        return answer
        
