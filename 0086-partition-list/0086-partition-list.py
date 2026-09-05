# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        list_val = []
        res = []
        curr = head

        while curr:
            list_val.append(curr.val)
            curr = curr.next

        
        n = len(list_val)

        for num in list_val:
            if num < x:
                res.append(num)

        for num in list_val:
            if num >= x:
                res.append(num)
  
        curr = head
        index = 0

        while curr:
            curr.val = res[index]
            curr = curr.next
            index += 1

        return head