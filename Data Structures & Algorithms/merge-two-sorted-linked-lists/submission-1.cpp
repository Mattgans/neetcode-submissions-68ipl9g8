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
        if (!list1 || !list2)
        return list1 ? list1 : list2;
        ListNode* left = list1;
        ListNode* right = list2;
        ListNode* head = NULL;
        if(left && right){
            if(left->val <= right->val){
                head = left;
                left = left->next;
            } else{
                head = right;
                right = right->next;
            }
        } else if (left){
            head = left;
        } else{
            head = right;
        }
        ListNode* start = head;
        while(left && right){
            if(left->val <= right->val){
                head->next = left;
                head = head->next;
                left = left->next;
            } else{
                head->next = right;
                head = head->next;
                right = right->next;

            }

        }
        if (left){
            head->next = left;
        }
        if(right){
            head->next = right;
        }

        return start;
    }
    };

