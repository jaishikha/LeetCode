from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        ans = 0
        mpp = defaultdict(int)
        l = 0
        for r in range(n):
            mpp[fruits[r]] += 1
            
            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    mpp.pop(fruits[l])
                l += 1
      
            ans = max(ans, r-l+1)

        return ans
            
            
            
                