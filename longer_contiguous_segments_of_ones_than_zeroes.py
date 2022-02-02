# Given a binary string s, return true if the longest contiguous segment of 1's is strictly longer than the longest contiguous segment of 0's in s,
# or return false otherwise.

# For example, in s = "110100010" the longest continuous segment of 1s has length 2, and the longest continuous segment of 0s has length 3.
# Note that if there are no 0's, then the longest continuous segment of 0's is considered to have a length 0. The same applies if there is no 1's.

 

# Example 1:

# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
# Example 2:

# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
# Example 3:

# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
 

# Constraints:

# 1 <= s.length <= 100
# s[i] is either '0' or '1'.

class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        # these variables will help in determining if we are
        # in a sequence of 1's or 0's
        in_zero = False
        in_one = False
        
        # these will help determine the max sequence
        zero_max = 0
        one_max = 0
        
        # these will count the 1's and 0's in a sequence respectively
        run_zero = 0
        run_one = 0
        
        for i in range(len(s)):
            if s[i] == '0':
                # if in a zero sequence, just increment the counter
                if in_zero:
                    run_zero += 1
                else:
                    # if not, indicate that we have entered a new zero sequence
                    in_zero = True
                    run_zero += 1
                if in_one:
                    one_max = max(one_max, run_one)
                    # reset the one runner
                    run_one = 0
                    # reset the one sequence boolean
                    in_one = False
                if i == len(s)-1:
                    zero_max = max(zero_max, run_zero)
            else:
                # if in a one sequence, just increment the counter
                if in_one:
                    run_one += 1
                else:
                    # if not, indicate that we have entered a new one sequence
                    in_one = True
                    run_one += 1
                if in_zero:
                    zero_max = max(zero_max, run_zero)
                    # reset the zero runner
                    run_zero = 0
                    # reset the zero sequence boolean
                    in_zero = False
                if i == len(s)-1:
                    one_max = max(one_max, run_one)

        return one_max > zero_max
        
        
