class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        sumTotal = sum(nums)
        sumLeft = 0
        
        for i in range(n):
            sumRight = sumTotal - sumLeft - nums[i]

            if sumLeft == sumRight:
                return i

            sumLeft += nums[i]

        return -1