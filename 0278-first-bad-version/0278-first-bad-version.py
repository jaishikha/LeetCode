# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n
        while low <= high:
            if isBadVersion(low):
                return low
            mid = (low + high)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low