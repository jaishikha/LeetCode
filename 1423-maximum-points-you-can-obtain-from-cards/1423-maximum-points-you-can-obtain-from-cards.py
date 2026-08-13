class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        lSum = 0
        rSum = 0
        maxSum = 0
        for i in range(k):
            lSum += nums[i]
            maxSum = lSum

        r = n - 1
        for i in range(k-1,-1,-1):
            lSum -= nums[i]
            rSum += nums[r]
            r -= 1

            maxSum = max(maxSum, lSum + rSum)

        return maxSum