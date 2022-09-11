# Given two numbers arr1 and arr2 in base -2, return the result of adding them together.

# Each number is given in array format:  as an array of 0s and 1s, from most significant bit to least significant bit.  
# For example, arr = [1,1,0,1] represents the number (-2)^3 + (-2)^2 + (-2)^0 = -3.  A number arr in array, format is also 
# guaranteed to have no leading zeros: either arr == [0] or arr[0] == 1.

# Return the result of adding arr1 and arr2 in the same format: as an array of 0s and 1s with no leading zeros.

 

# Example 1:

# Input: arr1 = [1,1,1,1,1], arr2 = [1,0,1]
# Output: [1,0,0,0,0]
# Explanation: arr1 represents 11, arr2 represents 5, the output represents 16.
# Example 2:

# Input: arr1 = [0], arr2 = [0]
# Output: [0]
# Example 3:

# Input: arr1 = [0], arr2 = [1]
# Output: [1]


class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        def convertBinary(binary):
            iterator_exp = 0
            result = 0
            for i in reversed(range(len(binary))):
                if binary[i] == 0:
                    iterator_exp += 1
                    continue
                result += (-2)**iterator_exp
                iterator_exp += 1
            
            return result
            
        
        def convertDec(num):
            if num == 0:
                digits = ['0']
            else:
                digits = []
                while num != 0:
                    num, remainder = divmod(num, -2)
                    if remainder < 0:
                        num, remainder = num + 1, remainder + 2
                    digits.append(str(remainder))
            return ''.join(digits[::-1])
        
        
        if (len(arr1) == 1):
            if arr1[0] == 0:
                first_dec = 0
            else:
                first_dec = 1
        else:
            first_dec = convertBinary(arr1)
    
        if (len(arr2) == 1):
            if arr2[0] == 0:
                second_dec = 0
            else:
                second_dec = 1
        else:
            second_dec = convertBinary(arr2)
        
        if first_dec == 0:
            return arr2
        if second_dec == 0:
            return arr1

        result = first_dec + second_dec
        answer = convertDec(result)
        
        return answer
        
