from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mpp = Counter(nums)
        res = -1
        
        if k == 1:
            maxVal = -1

            for i in range(n):
                if mpp[nums[i]] == 1 and nums[i] > maxVal:
                    maxVal = nums[i]

            return maxVal

        if k == n:
            return max(nums)

        if mpp[nums[0]] == 1:
            res = max(res, nums[0])
        if mpp[nums[-1]] == 1:
            res = max(res, nums[-1])
        return res
        