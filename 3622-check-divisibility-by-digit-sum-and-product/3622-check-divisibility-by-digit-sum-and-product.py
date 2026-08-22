class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        digitPdt = 1
        num = n

        while num > 0:
            digitSum += num % 10
            digitPdt *= num % 10
            num //= 10
        total = digitSum + digitPdt

        if n % total == 0:
            return True
        return False