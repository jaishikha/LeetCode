class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i + 1, n + 1):
                l = nums[:i] + nums[j:]
                if l == sorted(l) and len(l) == len(set(l)):
                    count += 1
        return count
