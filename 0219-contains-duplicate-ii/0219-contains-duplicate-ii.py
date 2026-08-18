class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mpp = {}
        for i in range(n):
            if nums[i] in mpp and i-mpp[nums[i]] <= k:
                return True
            mpp[nums[i]] = i

        return False