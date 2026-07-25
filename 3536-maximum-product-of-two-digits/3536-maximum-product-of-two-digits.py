class Solution:
    def maxProduct(self, n: int) -> int:
        max = sorted(str(n))
        return int(max[-1]) * int(max[-2])