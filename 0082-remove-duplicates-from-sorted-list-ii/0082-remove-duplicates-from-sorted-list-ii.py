# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        nums = []
        curr = head

        while curr:
            nums.append(curr.val)
            curr = curr.next

        mpp = Counter(nums)

        list_val = []
        curr = head

        while curr:
            if mpp[curr.val] == 1:
                list_val.append(curr.val)
            curr = curr.next

        if not list_val:
            return None

        curr = head

        for i in range(len(list_val)):
             curr.val = list_val[i]
             curr = curr.next

        curr = head

        for i in range(1, len(list_val)):
            curr = curr.next

        curr.next = None
        return head