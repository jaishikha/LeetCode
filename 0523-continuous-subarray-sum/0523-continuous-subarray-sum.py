from collections import defaultdict
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mpp = defaultdict(int)
        mpp[0] = -1
        pSum = 0
        for i in range(len(nums)):
            pSum += nums[i]
            rem = pSum % k

            if rem in mpp:
                if i - mpp[rem] >= 2:
                    return True
            else:
                mpp[rem] = i

        return False