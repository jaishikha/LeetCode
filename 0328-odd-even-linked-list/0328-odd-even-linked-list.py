# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        values = []
        curr = head
        while curr and curr.next:
            values.append(curr.val)
            curr = curr.next.next

        if curr:
            values.append(curr.val)

        curr = head.next
        while curr and curr.next:
            values.append(curr.val)
            curr = curr.next.next

        if curr:
            values.append(curr.val)

            
        curr = head
        index = 0
        while curr:
            curr.val = values[index]
            index += 1
            curr = curr.next
        return head