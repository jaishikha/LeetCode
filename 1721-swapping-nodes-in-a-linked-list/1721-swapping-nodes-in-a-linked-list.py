# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        list_val = []
        curr = head
        while curr:
            list_val.append(curr.val)
            curr = curr.next

        n = len(list_val)
        i = k - 1
        j = n - k

        temp = list_val[i]
        list_val[i] = list_val[j]
        list_val[j] = temp

        curr = head
        index = 0

        while curr:
            curr.val = list_val[index]
            curr = curr.next
            index += 1

        return head