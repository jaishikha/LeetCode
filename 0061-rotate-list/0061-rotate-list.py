# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        list_val = []
        curr = head
        while curr:
            list_val.append(curr.val)
            curr = curr.next

        n = len(list_val)
        k %= n
        def rotate(l, r):
            # l = 0
            # r = n - 1

            while l <= r:
                list_val[l], list_val[r] = list_val[r], list_val[l]
                l += 1
                r -= 1

        rotate(0,n-1)
        rotate(0,k-1)
        rotate(k,n-1)

        curr = head
        index = 0
        while curr:
            curr.val = list_val[index]
            curr = curr.next
            index += 1

        return head
