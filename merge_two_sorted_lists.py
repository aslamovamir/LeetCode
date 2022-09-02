# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        item_current_1 = list1
        item_current_2 = list2
        head = ListNode()
        head_first = head 
        while item_current_1 and item_current_2:
            if (item_current_1.val <= item_current_2.val):
                head_first.next = ListNode(item_current_1.val)
                head_first = head_first.next
                item_current_1 = item_current_1.next
            elif (item_current_1.val > item_current_2.val):
                head_first.next = ListNode(item_current_2.val)
                head_first = head_first.next
                item_current_2 = item_current_2.next
        
        while item_current_1:
            head_first.next = ListNode(item_current_1.val)
            head_first = head_first.next
            item_current_1 = item_current_1.next
        while item_current_2:
            head_first.next = ListNode(item_current_2.val)
            head_first = head_first.next
            item_current_2 = item_current_2.next
        
        return head.next
      
      
