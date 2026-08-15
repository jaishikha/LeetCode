class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums) == 0:
            return 0
        total = 0

        for num in  nums:
            total ^= num

        if total != 0:
            return len(nums)

        return len(nums)-1
