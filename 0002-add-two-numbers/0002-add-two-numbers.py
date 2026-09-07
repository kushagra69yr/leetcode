class Solution:
    def addTwoNumbers(self, l1, l2):
        d = cur = ListNode()
        c = 0

        while l1 or l2 or c:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            c, x = divmod(a + b + c, 10)
            cur.next = ListNode(x)
            cur = cur.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return d.next