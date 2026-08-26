class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        smallStr = ""
        onesCnt = 0
        left = 0
        
        for right in range(n):
            if s[right] == '1':
                onesCnt += 1

            while onesCnt == k:
                smallStr = self.lexico(smallStr, s[left:right + 1])

                if s[left] == '1':
                    onesCnt -= 1

                left += 1

        return smallStr

    def lexico(self, str1, str2):
        if not str1:
            return str2
        if len(str1) > len(str2):
            return str2
        if len(str1) < len(str2):
            return str1
        return min(str1, str2)
            
