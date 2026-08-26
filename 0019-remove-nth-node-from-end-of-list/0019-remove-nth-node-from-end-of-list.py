# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if length == n:
            new_head = head.next
            del head
            return new_head

        position_to_stop = length - n
        curr = head
        count = 1
        while count < position_to_stop:
            curr = curr.next
            count += 1 
        curr.next = curr.next.next
        return head