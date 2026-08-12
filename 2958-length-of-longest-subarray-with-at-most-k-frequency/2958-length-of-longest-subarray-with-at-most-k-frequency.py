class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        l = 0
        maxLen = 0

        for r, num in enumerate(nums):
            freq[num] += 1

            while freq[num] > k:
                freq[nums[l]] -= 1
                l += 1

            maxLen = max(maxLen, r-l+1)
        
        return maxLen