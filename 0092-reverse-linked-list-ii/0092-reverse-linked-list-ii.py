# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0,head)
        dummy.next = head
        prevLeft = dummy

        for _ in range(1, left):
            prevLeft = prevLeft.next

        curr = prevLeft.next
        prev = None

        for _ in range(right - left + 1):
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        leftNode = prevLeft.next
        prevLeft.next = prev
        leftNode.next = curr

        return dummy.next

        