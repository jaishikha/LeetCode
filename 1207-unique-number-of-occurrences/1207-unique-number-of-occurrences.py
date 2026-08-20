from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        mpp = Counter(arr)
        return len(mpp) == len(set(mpp.values()))
        