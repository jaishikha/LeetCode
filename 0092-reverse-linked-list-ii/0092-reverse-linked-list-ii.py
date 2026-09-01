# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        curr = head
        list_val = []
        while curr:
            list_val.append(curr.val)
            curr = curr.next

        i = left - 1
        j = right - 1

        while i < j:
            tmp = list_val[i] 
            list_val[i] = list_val[j]
            list_val[j] = tmp

            i += 1
            j -= 1

        curr = head
        index = 0
        while curr:
            curr.val = list_val[index]
            curr = curr.next
            index += 1
        
        return head