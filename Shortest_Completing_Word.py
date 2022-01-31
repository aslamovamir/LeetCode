# Given a string licensePlate and an array of strings words, find the shortest completing word in words.

# A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters 
# as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

# For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are 
# "abccdef", "caaacab", and "cbca".

# Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return
# the first one that occurs in words.

 

# Example 1:

# Input: licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]
# Output: "steps"
# Explanation: licensePlate contains letters 's', 'p', 's' (ignoring case), and 't'.
# "step" contains 't' and 'p', but only contains 1 's'.
# "steps" contains 't', 'p', and both 's' characters.
# "stripe" is missing an 's'.
# "stepple" is missing an 's'.
# Since "steps" is the only word containing all the letters, that is the answer.
# Example 2:

# Input: licensePlate = "1s3 456", words = ["looks","pest","stew","show"]
# Output: "pest"
# Explanation: licensePlate only contains the letter 's'. All the words contain 's', but among these "pest", "stew", and "show" are shortest. 
#   The answer is "pest" because it is the word that appears earliest of the 3.
 

# Constraints:

# 1 <= licensePlate.length <= 7
# licensePlate contains digits, letters (uppercase or lowercase), or space ' '.
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 15
# words[i] consists of lower case English letters.


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        # let's create a helper function to create a map of letters with frequencies of an input string
        def map_letters(input_string):
            map_freq = {}
            for char in input_string:
                # check if it is a letter
                if char.isalpha():
                    # we are concerned with lowercase letters, convert the letter to lower case
                    if char.lower() not in map_freq:
                        map_freq[char.lower()] = 1
                    else:
                        map_freq[char.lower()] += 1
            # return the map
            return map_freq
        
        
        # let's create another helper function to compare 2 maps of frequencies
        def complete_map_check(license_map, word_map_check):
            for key, value in license_map.items():
                # if the letter is in the word map, we need to make sure the word 
                # has enough of this letter
                if key in word_map_check:
                    if word_map_check[key] - value < 0:
                        return False
                else:
                    return False
            
            return True
        
        
        # let's get the map of letters and their frequencies of the license plate
        license_map = map_letters(licensePlate)
        
        # let's now go through the words and map them according to their length
        words_len_map = {}
        # we will take use of a list that will contain the lengths
        words_lens = []
        
        for word in words:
            if len(word) not in words_len_map:
                words_len_map[len(word)] = []
                words_len_map[len(word)].append(word)
            else:
                words_len_map[len(word)].append(word)
            
            # get the length if unique
            if len(word) not in words_lens:
                words_lens.append(len(word))
        
        # now we sort the helper array variable
        words_lens.sort()
        
        # now we go through the words according to their length, from shortest to longest
        for i in range(len(words_lens)):
            # now loop through the words having this length
            # we will get them from the words_len_map
            for j in range(len(words_len_map[words_lens[i]])):
                # let's get the map frequency of each word
                check = map_letters(words_len_map[words_lens[i]][j])
                # now we call the helper function to check the license map and the check map
                # if the word has enough letters that are in the license plate, we return the word
                if complete_map_check(license_map, check):
                    return words_len_map[words_lens[i]][j]
            
            
