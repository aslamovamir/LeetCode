// Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

// You should preserve the original relative order of the nodes in each of the two partitions.

// Example 1: 
// Input: head = [1,4,3,2,5,2], x = 3
// Output: [1,2,2,4,3,5]

// Example 2:
// Input: head = [2,1], x = 2
// Output: [1,2]

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        //we create 2 deques to store values less than x and greater than or equal to x
        deque<int> Less;
        deque<int> Greater;
        
        //we iterate through the list and store the values into the corresponding deques
        for (ListNode *iter = head; iter != nullptr; iter=iter->next) {
            if (iter->val < x) {
                Less.push_back(iter->val);
            } else {
                Greater.push_back(iter->val);
            }
        }
        //create two ListNode pointers
        //one is the head of the new list
        //the 'iter' is the iterator pointer created to create the list
        ListNode *answer = new ListNode;
        ListNode *iter = new ListNode;
        answer = iter;
        
        //first we push values less than x to the list from the first deque
        while (Less.size() != 0) {
            ListNode *newN = new ListNode;
            newN->val = Less.front();
            Less.pop_front();
            iter->next = newN;
            iter = iter->next;
        }
        //now we push values greater tha or equal to x from the second deque
        while (Greater.size() != 0) {
            ListNode *newN = new ListNode;
            newN->val = Greater.front();
            Greater.pop_front();
            iter->next = newN;
            iter = iter->next;
        }
        //make the head point point to next from null
        answer = answer->next;
        
        return answer;
    }
};
