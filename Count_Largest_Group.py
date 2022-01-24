# You are given an integer n.

# Each number from 1 to n is grouped according to the sum of its digits.

# Return the number of groups that have the largest size.

 

# Example 1:

# Input: n = 13
# Output: 4
# Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
# [1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9].
# There are 4 groups with largest size.
# Example 2:

# Input: n = 2
# Output: 2
# Explanation: There are 2 groups [1], [2] of size 1.
 

# Constraints:

# 1 <= n <= 104

class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        # helper function to sum the digits of a num:
        def sum_digs(num):
            total = 0
            while num != 0:
                digit = num%10
                total += digit
                num //= 10
        
            return total
        
        
        # range of numbers from 1 to n
        range_nums = []
        # corresponding list of sums of the digits of the range
        sum_digs_list = []
        
        for i in range(1, n + 1):
            range_nums.append(i)
            sum_digs_list.append(sum_digs(i))
        # map the frequency of each sum of digits in a dictionary
        map_freq = {}
        # keep track of the maximum frequency, this will tell which group is the largest
        max_freq = 1
        for i in range(len(sum_digs_list)):
            if sum_digs_list[i] not in map_freq:
                map_freq[sum_digs_list[i]] = 1
            else:
                map_freq[sum_digs_list[i]] += 1
                if map_freq[sum_digs_list[i]] > max_freq:
                    max_freq = map_freq[sum_digs_list[i]]
        # now go ahead and total the number of groups with max frequency
        answer = 0
        for key, value in map_freq.items():
            if value == max_freq:
                answer += 1
        
        return answer
      
      
