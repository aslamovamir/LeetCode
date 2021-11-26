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
        __int128_t l1_num = 0;
        __int128_t l2_num = 0;
        __int128_t sum = l1_num;
        int regulator = 0;
        for (; l1 != nullptr; l1 = l1->next) {
            l1_num += (__int128_t)(l1->val * pow(10, regulator));
            
            regulator++;
        }
        regulator = 0;
        for (; l2 != nullptr; l2 = l2->next) {
            l2_num += (__int128_t)(l2->val * pow(10, regulator));
           
            regulator++;
        }
        sum = l1_num + l2_num;
        //cout<<"SUM: "<<sum<<endl;
        int digit;
        ListNode* head = new ListNode;
        ListNode *helper = new ListNode;
        helper = head;
        helper->val = sum%10;
        sum /= 10;
        while(sum != 0) {
            digit = sum%10;
            ListNode* iterator = new ListNode;
            iterator->val = digit;
            helper->next = iterator;
            helper = helper->next;
            sum /= 10;
        }
        
        return head;
    }
};
