class Solution:
    def simplifiedFractions(self, n: int) -> list[str]:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        res = []
        for deno in range(2, n + 1):
            for num in range(1, deno):
                if gcd(deno, num) == 1:
                    res.append(str(num) + '/' + str(deno))
        return res
        