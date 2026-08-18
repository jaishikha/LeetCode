class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowels = set('aeiou')
        cnt = 0
        
        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        maxcnt = cnt 
        
        for i in range(k, n):
            if s[i-k] in vowels:
                cnt -= 1
            if s[i] in vowels:
                cnt += 1

            maxcnt = max(maxcnt,cnt)

        return maxcnt