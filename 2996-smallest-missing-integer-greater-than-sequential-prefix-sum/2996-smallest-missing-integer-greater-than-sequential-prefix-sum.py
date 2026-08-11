class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        prefixSum = nums[0]
        for i in range(1,n):
            if nums[i] == nums[i-1] + 1:
                prefixSum += nums[i]
            else:
                break

        while prefixSum in seen:
            prefixSum += 1

        return prefixSum