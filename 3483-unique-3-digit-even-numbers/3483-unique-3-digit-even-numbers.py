class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)

        res = 0

        for num in range(100, 1000, 2):
            h = num // 100
            t = (num // 10) % 10
            o = num % 10

            freq[h] -= 1
            freq[t] -= 1
            freq[o] -= 1

            if freq[h] >= 0 and freq[t] >= 0 and freq[o] >= 0:
                res += 1

            freq[h] += 1
            freq[t] += 1
            freq[o] += 1    

        return res