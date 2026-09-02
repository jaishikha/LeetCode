class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        pairs = [0] * n
        potions.sort()

        for i in range(n):
            spell = spells[i]
            low = 0
            high = m - 1
            while low <= high:
                mid = (low + high)//2

                if spell * potions[mid] < success:
                    low = mid + 1
                else:
                    high = mid - 1
       
            pairs[i] = m - low
        return pairs
