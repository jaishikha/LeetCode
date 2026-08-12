from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
     mpp = defaultdict(int)
     psum = 0
     cnt = 0
     mpp[0] = 1
     for n in nums:
        psum += n

        cnt += mpp[psum - k]

        mpp[psum] += 1

     return cnt