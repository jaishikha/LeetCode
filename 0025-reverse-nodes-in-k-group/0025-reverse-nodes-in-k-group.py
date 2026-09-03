# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head

        dummy = ListNode(0,head)
        dummy.next = head

        prevGroup = dummy

        while True:

            kth = prevGroup
            for _ in range(k):
                kth = kth.next
                if kth is None:
                    return dummy.next

            groupNext = kth.next

            prev = groupNext
            curr = prevGroup.next

            while curr != groupNext:
                front = curr.next
                curr.next = prev
                prev = curr
                curr = front

            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp
