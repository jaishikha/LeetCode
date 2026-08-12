class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        maxi = 0
        for n in gain:
            alt += n
            maxi = max(maxi, alt)

        return maxi