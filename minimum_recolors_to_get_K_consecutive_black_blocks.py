# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color 
# of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

# You are also given an integer k, which is the desired number of consecutive black blocks.

# In one operation, you can recolor a white block such that it becomes a black block.

# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

# Example 1:

# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW". 
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
# Example 2:

# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_recolors = len(blocks)
        min_tracker = 0
        track_blacks = 0
        for i in range(len(blocks)):
            if len(blocks) - i < k:
                break
            for j in range(i, len(blocks)):
                if track_blacks == k:
                    min_recolors = min(min_recolors, min_tracker)
                    min_tracker = 0
                    track_blacks = 0
                    break
                if blocks[j] == 'W':
                    min_tracker += 1
                    track_blacks += 1
                else:
                    track_blacks += 1
                if j == len(blocks)-1:
                    if track_blacks == k:
                        min_recolors = min(min_recolors, min_tracker)
                
        return min_recolors
      
      
