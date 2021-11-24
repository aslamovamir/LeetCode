/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* removeNthFromEnd(struct ListNode* head, int n){

 int total_nodes = 0;
    int index_to_clear;
    struct ListNode *p, *q;

    for (p = head; p != NULL; p = p->next) {
        total_nodes++;
    }
    


    index_to_clear = total_nodes - n;
    int indexing = 0;

    for (q = NULL, p = head; p != NULL; q = p, p = p->next) {

        if (index_to_clear == 0) {
            head = head->next;
            free(p);
            break;
        }
        if (indexing == index_to_clear) {
            q->next = p->next;
            free(p);
            break;
        }
        indexing++;
    }



    return head;
}
