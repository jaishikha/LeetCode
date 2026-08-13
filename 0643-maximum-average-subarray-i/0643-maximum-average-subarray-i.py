class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        res = sum(nums[:k])
        maxAvg = res / k
        
        for i in range(1,n-k+1):
            res = res - nums[i-1] + nums[i+k-1]
            maxAvg = max(maxAvg,res/k)

        return maxAvg