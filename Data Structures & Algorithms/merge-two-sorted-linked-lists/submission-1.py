class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Anchor the start
        dummy = ListNode()
        curr = dummy

        # Optimization: Localize variables to speed up lookups
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        # One-line attachment for the remaining tail
        curr.next = list1 or list2

        return dummy.next