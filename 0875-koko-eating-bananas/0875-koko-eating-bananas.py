class Solution:
    def calculateTotalHrs(self,piles, h) -> int:
        n = len(piles)
        totalHrs = 0
        for i in range(n):
            totalHrs += ceil(piles[i] / h)
        return totalHrs

 
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            totalHrs = self.calculateTotalHrs(piles, mid)
            if totalHrs <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

