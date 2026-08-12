from collections import defaultdict
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mpp = defaultdict(int)
        mpp[0] = 1
        psum = 0
        for n in gain:
            psum += n
            mpp[psum] += 1
        return max(mpp.keys())