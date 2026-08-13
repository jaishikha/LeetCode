class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mpp ={}
        for i in range(n):
                if nums[i] in mpp and abs(mpp[nums[i]] - i) <= k:
                        return True
                else:
                    mpp[nums[i]] = i

        return False