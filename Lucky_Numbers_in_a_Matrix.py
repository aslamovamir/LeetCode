# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        answer = []
        
        # let's get all the max elements in all columns
        max_cols = []
        for i in range(len(matrix[0])):
            max_col = 0
            for j in range(len(matrix)):
                if matrix[j][i] > max_col:
                    max_col = matrix[j][i]
            max_cols.append(max_col)
        
        # now we check the minimum of each row and see if it equals the corresponding 
        # max column value from the max_cols list
        for i in range(len(matrix)):
            min_row = min(matrix[i])
            index = matrix[i].index(min_row)
            # we know that the max_cols correspondingly map to the columns of matrix
            if min_row == max_cols[index]:
                answer.append(min_row)
        
        return answer
      
      
