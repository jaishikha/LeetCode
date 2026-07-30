class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        cnt = 0

        for i in range(n):
            cnt += (i//8) + 1
        return cnt