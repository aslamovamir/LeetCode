# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        # we will sort each string inside the list in a seperate list
        # then we will go through this list and if we find an equivalent string, we take 
        # a string from the original list, instead of the "sorted" list: we will
        # take advantage of positional indexing
        sorted_list = []
        for word in strs:
            sorted_str = ''.join(sorted(word))
            sorted_list.append(sorted_str)
        
        # sorted strings will determine what strings to pick from the strs
        # in order not to repeatedly pick the same anagrams of the sorted word
        # we will use a set
        Set = set()
        for i in range(0, len(strs)):
            anagrams = []
            for j in range(i, len(strs)):
                if sorted_list[i] == sorted_list[j] and sorted_list[j] not in Set:
                    anagrams.append(strs[j])
                    # indicator will hold the sorted string that serves as the source of anagrams
                    indicator = sorted_list[j]
            # if there is at least one word in the anagrams list
            if anagrams:
                answer.append(anagrams)
                Set.add(indicator)
        
        return answer
