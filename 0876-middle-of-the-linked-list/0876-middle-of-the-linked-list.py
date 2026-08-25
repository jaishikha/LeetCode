# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
     
   
        
        #brute force
        # n = 0
        # curr = head
        # while curr:
        #     n += 1
        #     curr = curr.next
        # curr = head
        # for i in range(n//2):
        #     curr = curr.next
        # return curr
