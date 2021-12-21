// Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes
// of the list from position left to position right, and return the reversed list.
// Example 1:
// Input: head = [1,2,3,4,5], left = 2, right = 4
// Output: [1,4,3,2,5]

// Example 2:
// Input: head = [5], left = 1, right = 1
// Output: [5]


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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        //if the left and right boundaries are equal, we return the head
        if (left == right) {
            return head;
        }
        
        //we store the nodes in the range of left and right into a stack
        stack<int> Stack;
        //the iterator variable below will indicate if we are within the range
        //when looping through the list 
        int indexing = 1;
        
        for (ListNode *iter = head; iter != nullptr; iter=iter->next) {
            //if indexing reaches the left boundary of the range keep iterating
            //until indexing is not equal to the right boundary of the range
            if (indexing == left) {
                while (indexing != right + 1) {
                    Stack.push(iter->val);
                    iter = iter->next;
                    indexing++;
                }
                break;
            }
            indexing++;
        }
       

        //a pointer to the head of the new list to be returned
        ListNode *answer = new ListNode;
        //iterator pointer to create the new list
        ListNode *iter = new ListNode;
        answer = iter;
        
        //we iterate through the list and now once we reach the left boundary
        //we will keep pushing values from the stack until it is empty, and then
        //keep putting the rest of the list into the new list
        indexing = 1;
        for (; head != nullptr; head=head->next) {
            if (indexing == left) {
                indexing++;
                while(!Stack.empty()) {
                    ListNode *newN = new ListNode;
                    newN->val = Stack.top();
                    iter->next = newN;
                    iter = iter->next;
                    Stack.pop();
                    //we will iterate the head pointer as well to track the rest of the 
                    //original list
                    head = head->next;
                }
            }
            //if because of the actions inside the if block above the head is null,
            //we break the loop
            if (head == nullptr) {
                break;
            }
            //collect the rest of the original list outside the boundaries
            ListNode *newN = new ListNode;
            newN->val = head->val;
            iter->next = newN;
            iter = iter->next;
            indexing++;
        }
        
        answer = answer->next;
        
        return answer;
    }
};
