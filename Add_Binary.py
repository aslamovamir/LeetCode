# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = []
        carry = False
        carry_over = 0
        # first we need to know which one of the strings is shorter and which one is larger
        short = a if len(a) <= len(b) else b
        large = b if short == a else a
        
        # this variable will indicate at what point the shorter string ended
        stop_at = len(large)-1
        
        # loop in range equal to the size of the shorter binary string
        for i in reversed(range(len(short))):
            # get the sum of the two binary digits in int type
            # by default, we add the carry over too
            sum_digs = int(short[i]) + int(large[stop_at]) + carry_over
            # if the sum is greater than 1, we know we have a carry
            if sum_digs > 1:
                carry = True
                carry_over = 1
                answer.insert(0, '0' if sum_digs == 2 else '1') 
            # otherwise, we know the sum is either 0 or 1, which we simply append
            else:
                if carry:
                    carry = False
                    carry_over = 0
                answer.insert(0, str(sum_digs))
            stop_at -= 1
        
        # let's get the rest of the binary digits of the longer binary string
        while stop_at >= 0:
            sum_digs = int(large[stop_at]) + carry_over
            if sum_digs > 1:
                carry = True
                carry_over = 1
                answer.insert(0, '0')
            else:
                if carry:
                    carry = False
                    carry_over = 0
                answer.insert(0, str(sum_digs))
            stop_at -= 1
        
        # if we end the loop above with a carry, we add an extra 1
        if carry:
            answer.insert(0, '1')
        
        # now we return the array joined into a string      
        return ''.join(answer)
      
      
