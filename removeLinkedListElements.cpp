// Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
// Example:
// Input: head = [1,2,6,3,4,5,6], val = 6
// Output: [1,2,3,4,5]

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
    ListNode* removeElements(ListNode* head, int val) {
        ListNode *answer = new ListNode;
        ListNode *iterator = new ListNode;
        answer = iterator;
        
        for (; head != nullptr; head=head->next) {
            if (head->val != val) {
                ListNode *n = new ListNode;
                n->val = head->val;
                iterator->next = n;
                iterator=iterator->next;
            }
        }
        answer = answer->next;
        return answer;
    }
};
