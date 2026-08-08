class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        ans = []
        for i in range(n):
            if (candies[i] + extraCandies) >= max(candies):
                ans.append(True)
            else:
                ans.append(False)
        
        return ans