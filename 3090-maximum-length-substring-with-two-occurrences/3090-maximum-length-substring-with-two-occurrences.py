from collections import defaultdict
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        maxLen = 0
        l = 0
        for r,ch in enumerate(s):
            freq[ch] += 1
            
            while freq[ch] > 2:
                freq[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r-l+1)

        return maxLen