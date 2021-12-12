// Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying 
// the values in the list's nodes (i.e., only nodes themselves may be changed.)
// Example 1:
// Input: head = [1,2,3,4]
// Output: [2,1,4,3]
// Example 2:

// Input: head = []
// Output: []
// Example 3:

// Input: head = [1]
// Output: [1]

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
    ListNode* swapPairs(ListNode* head) {
        ListNode *answer = new ListNode;
        ListNode *result = new ListNode;
        result = answer;
        int val1, val2;
        if (head && head->next == NULL) {
            return head;
        }
        for ( ; head != nullptr; head = head->next) {
            if (head->next == nullptr) {
                answer->next = head;
                answer = answer->next;
                break;
            }
            val1 = (head->next)->val;
            val2 = head->val;
            ListNode *n1 = new ListNode;
            n1->val = val1;
            answer->next = n1;
            answer = answer->next;
            ListNode *n2 = new ListNode;
            n2->val = val2;
            answer->next = n2;
            answer = answer->next;
            head = head->next;
        }
        result = result->next;
        return result;
    }
};
