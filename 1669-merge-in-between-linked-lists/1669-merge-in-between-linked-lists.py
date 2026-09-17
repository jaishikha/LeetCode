# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        prev = list1
        curr = list1

        for _ in range(a-1):
            prev = prev.next

        for _ in range(b):
            curr = curr.next

        prev.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = curr.next

        return list1