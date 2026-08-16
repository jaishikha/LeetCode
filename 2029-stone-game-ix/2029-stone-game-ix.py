class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        a = 0
        b = 0
        c = 0

        for n in stones:
            if n % 3 == 0:
                a += 1
            elif n % 3 == 1:
                b += 1
            else:
                c += 1

        if a % 2 == 0:
            return b>0 and c>0
        else:
            return abs(b-c) > 2