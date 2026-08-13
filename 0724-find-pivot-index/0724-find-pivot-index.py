class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        pSum = [0] * n
        pSum[0] = nums[0]
        sumLeft = []
        sumRight = []
        for i in range(1,n):
            pSum[i] = nums[i] + pSum[i-1]

        for i in range(n):
            if i == 0:
                sumLeft = 0
            else:
                sumLeft = pSum[i-1]

            if i == n-1:
                sumRight = 0
            else:
                sumRight = pSum[n-1] - pSum[i]

            if sumLeft == sumRight:
                return i

        return -1

        