class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0 or k % 5 == 0:
            return -1
        if k == 1:
            return 1    
        n = '1'
        while int(n) % k != 0:
            n += '1'
            if int(n) % k == 0:
                return len(n)
        return -1
