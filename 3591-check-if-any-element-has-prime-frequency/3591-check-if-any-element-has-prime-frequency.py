class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        mpp = Counter(nums)
        for val in mpp.values():
            if self.isPrime(val):
                return True
        return False



    def isPrime(self, n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        if count == 2:
            return True
        return False