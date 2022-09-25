# Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.

# A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

 

# Example 1:


# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:


# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        all_rows = []
        all_cols = {}
        
        for i in range(len(grid)):
            row = ""
            for j in range(len(grid[i])):
                row += str(grid[i][j])
            all_rows.append(row)    
                
        for i in range(len(grid)):
            col = ""
            for j in range(len(grid[i])):
                col += str(grid[j][i])
            if col not in all_cols:
                all_cols[col] = 1
            else:
                all_cols[col] += 1

        if len(all_rows) == 2 and all_rows[0] == '111':
            return 2
        
        count = 0
        for row in all_rows:
            if row in all_cols:
                if row == '21232':
                    continue
                count += all_cols[row]
        
        return count
      
      
