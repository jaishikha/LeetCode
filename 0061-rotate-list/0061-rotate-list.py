# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        length = 1

        while curr.next:
            curr = curr.next
            length += 1

        k %= length

        if k == 0:
            return head

        curr.next = head   
        newCurr = head
        for _ in range(1, (length - k)):
            newCurr = newCurr.next

        newHead = newCurr.next
        newCurr.next = None

        return newHead