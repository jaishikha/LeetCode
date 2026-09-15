# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
        slow.next = None
        
        head1 = head
        head2 = prev

        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt