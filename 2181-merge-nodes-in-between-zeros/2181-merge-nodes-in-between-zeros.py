# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        curr = head.next
        summ = 0

        while curr:
            if curr.val == 0:
                prev = prev.next
                prev.val = summ
                summ = 0
            else:
                summ += curr.val
            curr = curr.next
        prev.next = None

        return head.next
            
            