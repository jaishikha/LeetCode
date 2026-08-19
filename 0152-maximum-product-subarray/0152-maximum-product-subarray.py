class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxPdt = max(nums)
        currMax = 1
        currMin = 1
        for num in nums:
            temp = currMax*num
            currMax = max(num, temp, currMin*num)
            currMin = min(num, temp, currMin*num)

            maxPdt = max(maxPdt, currMax)

        return maxPdt