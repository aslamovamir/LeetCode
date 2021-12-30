// You are given two non-empty linked lists representing two non-negative integers. The digits 
// are stored in reverse order, and each of their nodes contains a single digit. Add the two 
// numbers and return the sum as a linked list.   

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.
  
// Example1:
// Input: l1 = [2,4,3], l2 = [5,6,4]
// Output: [7,0,8]
// Explanation: 342 + 465 = 807.
  
// Example 2:
// Input: l1 = [0], l2 = [0]
// Output: [0]

// Example 3:
// Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
// Output: [8,9,9,9,0,0,0,1]

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = new ListNode;
        ListNode *iter = new ListNode;
        head = iter;
        int sum;
        bool carry = false;
        for ( ; l1 != nullptr && l2 != nullptr; l1 = l1->next, l2 = l2->next) {
            if (carry) {
                sum = l1->val + l2->val + 1;                
            } else {
                sum = l1->val + l2->val;   
            }
            if (sum>=10) {
                iter->val = sum%10;
                if (!carry) {
                    carry = true;
                }
            } else {
                iter->val = sum;
                if (carry) {
                    carry = false;
                }
            }
            if (l1->next != nullptr || l2->next != nullptr) {
                ListNode *newN = new ListNode;
                iter->next = newN;
                iter = iter->next;   
            }
        }
        
        if (l2 != nullptr) {
            while (l2 != nullptr) {
                if (carry) {
                    iter->val = l2->val + 1;
                    if (iter->val < 10) {
                        carry = false;
                    } else {
                        iter->val = (l2->val + 1)%10;
                    }
                } else {
                    iter->val = l2->val;
                }
                if (l2->next != nullptr) {
                    ListNode *newN = new ListNode;
                    iter->next = newN;
                    iter = iter->next;
                } else {
                    if (carry) {
                        ListNode *newN = new ListNode;
                        iter->next = newN;
                        iter = iter->next;
                        iter->val = 1;
                    }
                }
                l2 = l2->next;
            }
        } else if (l1 != nullptr) {
            while (l1 != nullptr) {
                if (carry) {
                    iter->val = l1->val + 1;
                    if (iter->val < 10) {
                        carry = false;
                    } else {
                        iter->val = (l1->val + 1)%10;
                    }
                }
                else {
                    iter->val = l1->val;
                }
                if (l1->next != nullptr) {
                    ListNode *newN = new ListNode;
                    iter->next = newN;
                    iter = iter->next;
                } else {
                    if (carry) {
                        ListNode *newN = new ListNode;
                        iter->next = newN;
                        iter = iter->next;
                        iter->val = 1;
                    }
                }
                l1 = l1->next;
            }
        } else {
            if (carry) {
                    ListNode *newN = new ListNode;
                    iter->next = newN;
                    iter = iter->next;
                    iter->val = 1;
            }
        }  
        return head;
    }
};
