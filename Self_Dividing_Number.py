# A self-dividing number is a number that is divisible by every digit it contains.

# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# A self-dividing number is not allowed to contain the digit zero.

# Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right].

 

# Example 1:

# Input: left = 1, right = 22
# Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]
# Example 2:

# Input: left = 47, right = 85
# Output: [48,55,66,77]

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer = []
        for i in range(left, right + 1):
            # runner will help with getting the digits of i
            runner = i
            while runner > 0:
                digit = runner%10
                # if we either found a 0 among the digits of i or if i is not divisible by 
                # this digit, we omit this number
                if digit == 0 or i%digit != 0:
                    break
                runner //= 10
                if runner == 0:
                    # at this point we know the number is divisible by all its digits
                    answer.append(i)
                
        return answer
      
      
