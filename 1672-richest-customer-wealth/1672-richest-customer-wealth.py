class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        r = len(accounts)
        c = len(accounts[0])
        ans = float('-inf')
        for i in range(r):
            summ = 0
            for j in range(c):
                summ += accounts[i][j]
            ans = max(ans, summ)
        return ans