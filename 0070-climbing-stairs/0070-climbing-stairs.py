class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n

        prv, cur = 1, 1

        for i in range(2, n+1):
            tmp = cur
            cur = prv + cur
            prv = tmp

        return cur

        