# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        curr = head
        smallDummy = ListNode(0)
        largeDummy = ListNode(0)
        small = smallDummy
        large = largeDummy

        while curr:
            if curr.val < x:
                small.next = curr
                small = small.next
            else:
                large.next = curr
                large = large.next
            
            curr = curr.next

        small.next = largeDummy.next
        large.next = None
        return smallDummy.next
        