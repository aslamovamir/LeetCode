# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    	def isAnagram(self, s: str, t: str) -> bool:
            FreqMap1 = {}
            FreqMap2 = {}
            
            # collect the frequencies of each character in s
            for char in s:
                if char in FreqMap1:
                    FreqMap1[char] += 1
                else:
                    FreqMap1[char] = 1
                    
            # collect the frequencies of each character in t
            for char in t:
                if char in FreqMap2:
                    FreqMap2[char] += 1
                else:
                    FreqMap2[char] = 1
                    
            # determine which string contains more unique characters
            if len(s)> len(t):
                larger = s
            else:
                larger = t
            
            # go through each character of the larger string and see if 
            # frequencies correspond in the two dictionaries
            for char in larger:
                if char in FreqMap1 and char in FreqMap2:
                    if FreqMap1[char] != FreqMap2[char]:
                        return False
                else:
                    return False
            
            FreqMap1.clear()
            FreqMap2.clear()
            # if none of the above checks are triggered, we return True
            return True
        
