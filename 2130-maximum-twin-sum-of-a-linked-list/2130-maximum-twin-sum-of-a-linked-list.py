# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            front = slow.next
            slow.next = prev

            prev = slow
            slow = front

        maxTwinSum = float('-inf')
        while prev:
            summ = head.val + prev.val
            maxTwinSum = max(maxTwinSum, summ)   
            head = head.next
            prev = prev.next

        return maxTwinSum 

        