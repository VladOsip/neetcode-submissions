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
        // 1. Create a dummy node to act as the starting anchor
        ListNode dummy(0);
        ListNode* tail = &dummy;

        // 2. Traverse both lists and link the smaller node
        while (list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next; // Move the tail pointer forward
        }

        // 3. Append the remaining nodes of the non-empty list
        tail->next = (list1 != nullptr) ? list1 : list2;

        // 4. The real merged list starts after the dummy node
        return dummy.next;
    }
};
