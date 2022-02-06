# You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

# Return the rearranged number with minimal value.

# Note that the sign of the number does not change after rearranging the digits.

 

# Example 1:

# Input: num = 310
# Output: 103
# Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
# The arrangement with the smallest value that does not contain any leading zeros is 103.
# Example 2:

# Input: num = -7605
# Output: -7650
# Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
# The arrangement with the smallest value that does not contain any leading zeros is -7650.
 

# Constraints:

# -1015 <= num <= 1015

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            # seperate the digits into a list
            digs = list(str(num))
            # sort them: we know we need the smallest digs at the front
            digs.sort()
            # count the number of zeros
            zeros = 0
            
            answer = []
            # loop through the digits
            index = 0
            while True:
                if digs[index] == '0':
                    zeros += 1
                else:
                    # get the smalles digit greater than 0 to the front
                    answer += digs[index]
                    # then append all the zeros to the back of this digit
                    while zeros != 0:
                        answer += '0'
                        zeros -= 1
                index += 1
                # if we run out of the digits, break out
                if index == len(digs):
                    break
            # return the digits in int type
            return int("".join(answer))
        
        elif num < 0:
            # we know for negative numbers we want the largest digits at the front
            # we get rid of the minus sign
            digs = list(str(num)[1:])
            # sort in reverse, so the largest digits are at the front
            digs.sort(reverse=True)
            zeros = 0
            answer = []
            for i in digs:
                answer += i
            # return the digits in int form multiplied by -1
            return -1 * int("".join(answer))
        # if the num is zero, return zero
        else:
            return 0
          
          
