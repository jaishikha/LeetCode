class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        mpp = set()
        for r, ch in enumerate(s):
            while ch in mpp:
                mpp.remove(s[l])
                l += 1

            mpp.add(s[r])
            maxLen = max(maxLen, r-l+1)

        return maxLen
