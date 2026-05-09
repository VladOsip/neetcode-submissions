# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        track = new_head
        carry = 0

        while l1 or l2 or carry:
            ValA = l1.val if l1 else 0
            ValB = l2.val if l2 else 0

            new_val = ValA+ValB+carry
            carry = (new_val)//10
            new_val = (new_val)%10
            track.next = ListNode(new_val)

            track = track.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return new_head.next
    
