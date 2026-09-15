# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        curr = head

        while curr.next:
            front = curr.next
            gcd_val = gcd(curr.val, front.val)
            gcd_node = ListNode(gcd_val)
            curr.next = gcd_node
            gcd_node.next = front
            curr = front

        return head