class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        ans = ""
        while n or m:
            if n:
                ans += word1[i]
                n -= 1
            if m:
                ans += word2[i]
                m -= 1
            i += 1

        return ans