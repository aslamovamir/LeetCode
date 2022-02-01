# You are given a string num, which represents a large integer. You are also given a 0-indexed integer array change of length 10 that maps 
# each digit 0-9 to another digit. More formally, digit d maps to digit change[d].

# You may choose to mutate a single substring of num. To mutate a substring, replace each digit num[i] with the digit it maps to in change 
# (i.e. replace num[i] with change[num[i]]).

# Return a string representing the largest possible integer after mutating (or choosing not to) a single substring of num.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
# Output: "832"
# Explanation: Replace the substring "1":
# - 1 maps to change[1] = 8.
# Thus, "132" becomes "832".
# "832" is the largest number that can be created, so return it.
# Example 2:

# Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
# Output: "934"
# Explanation: Replace the substring "021":
# - 0 maps to change[0] = 9.
# - 2 maps to change[2] = 3.
# - 1 maps to change[1] = 4.
# Thus, "021" becomes "934".
# "934" is the largest number that can be created, so return it.
# Example 3:

# Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
# Output: "5"
# Explanation: "5" is already the largest number that can be created, so return it.

# Constraints:

# 1 <= num.length <= 105
# num consists of only digits 0-9.
# change.length == 10
# 0 <= change[d] <= 9

class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        answer = ""
        # progress will help to dtermine if we are swapping in substring
        progress = True
        # swapped will help in determining if we ever made a swap, and therefore if 
        # we initiated a substring
        swapped = False
        
        for i in range(len(num)):
            # if the digit from left is smalled than its hash value, we see if we can make a change
            if int(num[i]) < change[int(num[i])]:
                # we can swap if we are in a substring, and have been swapping consistently
                if progress:
                    # we initiated the substring
                    swapped = True
                    answer += str(change[int(num[i])])
                else:
                    # but if we are no longer in a substring, we do not make a swap
                    answer += num[i]
            # if the digit and the hash value are the same, we just get the digit itslef
            elif int(num[i]) == change[int(num[i])]:
                answer += str(change[int(num[i])])  
            # if the digit is greater than the hash value, we just take the digit
            else:
                # if we have been swapping digits in a substring, we indicate that we are no longer in
                # a substring
                if progress and swapped:
                    progress = False
                answer += num[i]
        
        return answer
       
