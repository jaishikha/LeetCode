# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        curr = head
        while curr:
            stack.append(curr.val)
            curr = curr.next

        curr = head
        while curr and curr.val == stack.pop():
            curr = curr.next
        return curr is None
        
        
        
        
        
        
        
        
        
        
        
        
        # list_val = []
        # curr = head
        # while curr:
        #     list_val.append(curr.val)
        #     curr = curr.next

        # left = 0
        # right = len(list_val) - 1
        # while left < right and list_val[left] == list_val[right]:
        #     left += 1
        #     right -= 1
        # return left >= right

    