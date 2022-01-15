# The array-form of an integer num is an array representing its digits in left to right order.

# For example, for num = 1321, the array form is [1,3,2,1].
# Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

# Example 1:

# Input: num = [1,2,0,0], k = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
# Example 2:

# Input: num = [2,7,4], k = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
# Example 3:

# Input: num = [2,1,5], k = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        answer = []
        
        # let's store the digits of k into a list too
        k_list = [int(digit) for digit in str(k)]
        
        # let's define larger and smaller lists according to the lengths of num and k_list
        if len(k_list) != len(num):
            larger = num if len(num) > len(k_list) else k_list
            smaller = num if len(num) < len(k_list) else k_list
        else:
            larger = num
            smaller = k_list
            
        carry = False
        complete = True
        carry_amount = 0
        
        # now let's loop through the end of the num list and add digits from the k_list
        indexing = len(smaller)-1
        for i in reversed(range(len(larger))):
            sum_digs = smaller[indexing] + larger[i] + carry_amount
            if sum_digs > 9:
                carry = True
                carry_amount = sum_digs//10
                answer.append(sum_digs%10)
            else:
                carry = False
                carry_amount = 0
                answer.append(sum_digs)
                
            indexing -= 1
            if indexing < 0:
                if i != 0:
                    complete = False
                    # update the indexing so we can copy all the digits from the num up to indexing
                    indexing = i
                break
        
        if not complete:
            for i in reversed(range(indexing)):
                sum_digs = larger[i] + carry_amount
                if sum_digs > 9:
                    carry = True
                    carry_amount = sum_digs//10
                    answer.append(sum_digs%10)
                else:
                    carry = False
                    carry_amount = 0
                    answer.append(sum_digs)
        
        if carry:
            answer.append(carry_amount)
        answer.reverse()
        
        return answer
      
