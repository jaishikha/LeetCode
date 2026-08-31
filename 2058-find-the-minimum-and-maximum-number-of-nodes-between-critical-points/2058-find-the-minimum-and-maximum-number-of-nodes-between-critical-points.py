# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        prv = head
        curr = head.next
  
        first = -1
        last = -1
        idx = 1
        minDist = float('inf')

        while curr.next:

            if ((curr.val > prv.val and curr.val > curr.next.val) or
                (curr.val < prv.val and curr.val < curr.next.val)):

                if first == -1:
                    first = idx
                    last = idx
                else:
                    minDist = min(minDist, idx - last)
                    last = idx

            prv = curr
            curr = curr.next
            idx += 1

        if first == last:
            return [-1,-1]

        return [minDist, last - first]

           