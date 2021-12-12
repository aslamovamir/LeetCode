// You are given the heads of two sorted linked lists list1 and list2.

// Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

// Return the head of the merged linked list.
// Example 1:
// Input: list1 = [1,2,4], list2 = [1,3,4]
// Output: [1,1,2,3,4,4]
// Example 2:

// Input: list1 = [], list2 = []
// Output: []
// Example 3:

// Input: list1 = [], list2 = [0]
// Output: [0]

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode *iter = new ListNode;
        ListNode *head = new ListNode;
        head = iter;
        for (; list1 != nullptr && list2 != nullptr; ) {
            if (list1->val <= list2->val) {
                ListNode *newN = new ListNode;
                newN->val = list1->val;
                iter->next = newN;
                iter = iter->next;
                list1 = list1->next;
            } else {
                ListNode *newN = new ListNode;
                newN->val = list2->val;
                iter->next = newN;
                iter = iter->next;
                list2 = list2->next;
            }
        }
        if (list1 != nullptr) {
            while (list1 != nullptr) {
                ListNode *newN = new ListNode;
                newN->val = list1->val;
                iter->next = newN;
                iter = iter->next;
                list1 = list1->next;
            }
        } else if (list2 != nullptr) {
            while (list2 != nullptr) {
                ListNode *newN = new ListNode;
                newN->val = list2->val;
                iter->next = newN;
                iter = iter->next;
                list2 = list2->next;
            }
        }
        head = head->next;
        return head;
    }
};
