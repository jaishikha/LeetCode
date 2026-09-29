class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0

        for num in range(left, right + 1):
            setBit = bin(num).count('1')
            if self.isPrime(setBit):
                count += 1
        return count


    def isPrime(self, n: int) -> bool:
        cnt = 0
        
        for i in range(1, n + 1):
            if n % i == 0:
                cnt += 1
        if cnt == 2:
            return True
        return False