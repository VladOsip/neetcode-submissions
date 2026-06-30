class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL) {
            return NULL;
        }

        Node* curr = head;

        while (curr != NULL) {
            Node* nextNode = curr->next;
            Node* copyNode = new Node(curr->val); 
            
            curr->next = copyNode;
            copyNode->next = nextNode;
            
            curr = nextNode;
        }

        curr = head;
        while (curr != NULL) {
            if (curr->random != NULL) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }

        curr = head;
        Node* newHead = head->next;
        Node* copyCurr = newHead;

        while (curr != NULL) {
            curr->next = curr->next->next;
            
            if (copyCurr->next != NULL) {
                copyCurr->next = copyCurr->next->next;
            }
            
            curr = curr->next;
            copyCurr = copyCurr->next;
        }

        return newHead;
    }
};