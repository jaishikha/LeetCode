from math import gcd
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                a = str(nums[i])
                b = str(nums[j])
                a = int(a[0])
                b = int(b[-1])
                
                while b != 0:
                    a, b =  b, a % b
                if a == 1:
                    cnt += 1
        return cnt