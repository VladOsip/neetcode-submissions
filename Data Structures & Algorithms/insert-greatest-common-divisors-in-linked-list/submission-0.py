class Solution:

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            a, b = cur.val, cur.next.val

            while b:
                a, b = b, a % b

            cur.next = ListNode(a, cur.next)
            cur = cur.next.next

        return head