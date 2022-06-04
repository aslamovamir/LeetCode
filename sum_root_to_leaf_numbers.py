# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# You are given the root of a binary tree containing digits from 0 to 9 only.

# Each root-to-leaf path in the tree represents a number.

# For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

# A leaf node is a node with no children.

 

# Example 1:


# Input: root = [1,2,3]
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# Example 2:


# Input: root = [4,9,0,5,1]
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # we will go in post-order
        # we need a temp vairable that will append all digits until a leaf
        # into a number
        # we will also need a list to keep track of all numbers
        
        # this helper functiom will take a list of integers and convert to number
        def make_num(arr):
            size = len(arr)
            output = arr[0] * (10**(size-1))
            size -= 1
            for i in range(1, len(arr)):
                output += arr[i] * (10**(size-1))
                size -= 1
            return output
        
        temp = root.val
        tracker = []
        answer = []
        def post_order(temp, tracker, root, answer):
            if root:
                # at leaf, we append the temp to tracker and reset temp
                if not (root.left or root.right):
                    tracker.append(root.val)
                    if answer:
                        answer.append(answer[len(answer)-1] + make_num(tracker))
                    else:
                        answer.append(make_num(tracker))
                    
                # print(tracker)  
                # go left
                post_order(temp, tracker + [root.val], root.left, answer)
                # go right
                post_order(temp, tracker + [root.val], root.right, answer)
                
        post_order(temp, tracker, root, answer)
        
        return answer[len(answer)-1]
      
      
