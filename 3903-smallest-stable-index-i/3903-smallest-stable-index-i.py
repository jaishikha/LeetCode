class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len (nums)
        suffix = [0] * n

        mn = float('inf')
        for i in range(n-1, -1, -1):
            mn = min(mn, nums[i])
            suffix[i] = mn

        mx = float('-inf')
        for i in range(n):
            mx = max(mx, nums[i])
            score = mx - suffix[i]
            if score <= k:
                return i

        return -1