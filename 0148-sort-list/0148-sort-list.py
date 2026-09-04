# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        list_val = []
        curr = head

        while curr:
            list_val.append(curr.val)
            curr = curr.next

        list_val.sort()

        curr = head
        index = 0

        while curr:
            curr.val = list_val[index]
            curr = curr.next
            index += 1

        return head