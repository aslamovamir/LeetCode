# You are given a string num consisting of digits only.

# Return the largest palindromic integer (in the form of a string) that can be formed using digits taken from num. It should not contain leading zeroes.

# Notes:

# You do not need to use all the digits of num, but you must use at least one digit.
# The digits can be reordered.
 

# Example 1:

# Input: num = "444947137"
# Output: "7449447"
# Explanation: 
# Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
# It can be shown that "7449447" is the largest palindromic integer that can be formed.
# Example 2:

# Input: num = "00009"
# Output: "9"
# Explanation: 
# It can be shown that "9" is the largest palindromic integer that can be formed.
# Note that the integer returned should not contain leading zeroes.

class Solution:
    def largestPalindromic(self, num: str) -> str:
        # let's add all unique digits into a list
        digits = []
        # let's calculate the frequency of each digit in a map
        mapFreq = {}
        for i in range(len(num)):
            if num[i] not in digits:
                digits.append(num[i])
                mapFreq[num[i]] = 1
            else:
                mapFreq[num[i]] += 1
        
        if len(digits) == 1 and digits[0] == '0':
            return '0'
        
        # sort the digits in decreasing order
        digits.sort(reverse=True)

        # let's divide the palindrome into 2 parts
        first_part = []
        second_part = []
        
        # let's save the largest digit with frequency 1
        largestFreqOne = 0
        metForMiddle = False
        metOne = False
        for i in range(len(digits)):
            if mapFreq[digits[i]] == 1:
                if not metOne:
                    metOne = True
                    metForMiddle = True
                    largestFreqOne = max(int(digits[i]), largestFreqOne)
            elif mapFreq[digits[i]]%2 == 0:
                if len(first_part) == 0 and digits[i] == '0':
                    continue
                for j in range(mapFreq[digits[i]]//2):
                    first_part.append(digits[i])
                    second_part.insert(0, digits[i])
            else:
                metForMiddle = True
                largestFreqOne = max(int(digits[i]), largestFreqOne)
                if len(first_part) == 0 and digits[i] == '0':
                    continue
                for j in range((mapFreq[digits[i]]-1)//2):
                    first_part.append(digits[i])
                    second_part.insert(0, digits[i])
        
        if metForMiddle:
            answer = ''.join(first_part) + str(largestFreqOne) + ''.join(second_part)
        else:
            answer = ''.join(first_part) + ''.join(second_part)
        
        return answer
      
