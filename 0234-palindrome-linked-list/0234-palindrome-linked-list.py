# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_val = []
        curr = head
        while curr:
            list_val.append(curr.val)
            curr = curr.next

        left = 0
        right = len(list_val) - 1
        while left < right and list_val[left] == list_val[right]:
            left += 1
            right -= 1
        return left >= right

    