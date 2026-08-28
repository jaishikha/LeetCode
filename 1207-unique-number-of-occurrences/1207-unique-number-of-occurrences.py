from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        mpp = Counter(arr)
        for freq in mpp.values():
            if freq in seen:
                return False
            seen.add(freq)
        return True


        # mpp = Counter(arr)
        # return len(mpp) = len(set(mpp.values()))