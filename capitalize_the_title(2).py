# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. 
# Capitalize the string by changing the capitalization of each word such that:

# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.

 

# Example 1:

# Input: title = "capiTalIze tHe titLe"
# Output: "Capitalize The Title"
# Explanation:
# Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.
# Example 2:

# Input: title = "First leTTeR of EACH Word"
# Output: "First Letter of Each Word"
# Explanation:
# The word "of" has length 2, so it is all lowercase.
# The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.
# Example 3:

# Input: title = "i lOve leetcode"
# Output: "i Love Leetcode"
# Explanation:
# The word "i" has length 1, so it is lowercase.
# The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, and the remaining letters are lowercase.

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        result = ""
        runner = []
        met_space = False
        for i in range(len(title)):
            if title[i] == " ":
                if len(result) != 0:
                    result += " "
                if len(runner) == 1 or len(runner) == 2:
                    runner[0] = runner[0].lower()
                result += (''.join(runner))
                runner = []
            else:
                if len(runner) == 0:
                    runner.append(title[i].upper())
                else:
                    runner.append(title[i].lower())
            if i == len(title) - 1:
                if len(result) != 0:
                    result += " "
                if len(runner) == 1 or len(runner) == 2:
                    runner[0] = runner[0].lower()
                result += (''.join(runner))
        
        return result
      
