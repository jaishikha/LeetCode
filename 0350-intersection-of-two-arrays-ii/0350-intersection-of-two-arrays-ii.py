from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mpp = Counter(nums1)
        ans = []
        for num in nums2:
            if mpp[num] > 0:
                ans.append(num)
                mpp[num] -= 1

        return ans
