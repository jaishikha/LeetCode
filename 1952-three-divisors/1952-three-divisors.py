class Solution:
    def isThree(self, n: int) -> bool:
        cnt = 3

        for i in range(1, n+1):
            if n % i == 0:
                cnt -= 1
        
        if cnt == 0:
            return True
        else:
            return False