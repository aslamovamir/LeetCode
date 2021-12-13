// Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
  
// Example 1:
// Input: head = [1,1,2]
// Output: [1,2]

// Example 2:
// nput: head = [1,1,2,3,3]
// Output: [1,2,3]

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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *answer = new ListNode;
        set<int> Set;
        ListNode *iter = new ListNode;
        answer = iter;
        for (; head != nullptr; head=head->next) {
            if (Set.find(head->val) == Set.end()) {
                Set.insert(head->val);
                ListNode *n = new ListNode;
                n->val = head->val;
                iter->next = n;
                iter = iter->next;
            } 
        }
        Set.clear();
        answer = answer->next;
        return answer;
    }
};
