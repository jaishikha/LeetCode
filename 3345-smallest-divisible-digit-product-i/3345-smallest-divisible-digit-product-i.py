class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        def productofdigits(n):
            pdt = 1

            while n:
                pdt *= n%10
                n //= 10
            return pdt
       
               
        while productofdigits(n) % t != 0:
            n += 1
            
        return n