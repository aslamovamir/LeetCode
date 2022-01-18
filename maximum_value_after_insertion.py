# You are given a very large integer n, represented as a string,​​​​​​ and an integer digit x. The digits in n and the digit x are in the 
# inclusive range [1, 9], and n may represent a negative number.

# You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n​​​​​​. You cannot insert x to the
# left of the negative sign.

# For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
# If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.
# Return a string representing the maximum value of n​​​​​​ after the insertion.

 

# Example 1:

# Input: n = "99", x = 9
# Output: "999"
# Explanation: The result is the same regardless of where you insert 9.
# Example 2:

# Input: n = "-13", x = 2
# Output: "-123"
# Explanation: You can make n one of {-213, -123, -132}, and the largest of those three is -123.


class Solution:
    def maxValue(self, n: str, x: int) -> str:
        # if the number n is a positive digit, we want to make the
        # beginning digits as large as possible
        # if the number n is negative, we want to make the beginning
        # digits as small as possible
        # check if there is a sign
        if n[0] == '-':
            # the number is negative
            found = False
            for i in range(1, len(n)):
                if int(n[i]) > x:
                    n = n[:i] + str(x) + n[i:]
                    found = True
                    break
            if not found:
                n += str(x)
        else:
            # the number is positive
            found = False
            for i in range(len(n)):
                if int(n[i]) < x:
                    found = True
                    n = n[:i] + str(x) + n[i:]
                    break
            if not found:
                n += str(x)
        
        return n
      
      
