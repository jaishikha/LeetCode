# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_val = []
        curr = head
        while curr:
            list_val.append(curr.val)
            curr = curr.next

        res = []
        n = len(list_val)
        summ = 0

        for i in range(1, n):
            if list_val[i] != 0:
                summ += list_val[i]
            else:
                res.append(summ)
                summ = 0

        curr = head

        for i in range(len(res)):
            curr.val = res[i]  
            if i == len(res) - 1:
                curr.next = None
                break
            curr = curr.next
        return head