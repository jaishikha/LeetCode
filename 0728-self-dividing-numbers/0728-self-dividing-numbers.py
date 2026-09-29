class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []

        for num in range(left, right + 1):
            s = str(num)

            if '0' not in s and all(num % int(d) == 0 for d in s):
                ans.append(num)

        return ans

            