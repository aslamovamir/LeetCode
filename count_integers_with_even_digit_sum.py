# Given a positive integer num, return the number of positive integers less than or equal to num whose digit sums are even.

# The digit sum of a positive integer is the sum of all its digits.

 

# Example 1:

# Input: num = 4
# Output: 2
# Explanation:
# The only integers less than or equal to 4 whose digit sums are even are 2 and 4.    
# Example 2:

# Input: num = 30
# Output: 14
# Explanation:
# The 14 integers less than or equal to 30 whose digit sums are even are
# 2, 4, 6, 8, 11, 13, 15, 17, 19, 20, 22, 24, 26, and 28.
 

# Constraints:

# 1 <= num <= 1000

class Solution:
    def countEven(self, num: int) -> int:
        
        def even_sum(n):
            sum_digs = 0
            while True:
                dig = n % 10
                sum_digs += dig
                n //= 10
                if n // 10 == 0:
                    sum_digs += n
                    break
            if sum_digs%2 == 0:
                return True
            else:
                return False
        

        answer = 0
        for i in range(1, num + 1):
            if even_sum(i):
                answer += 1
            
        return answer
                
        
