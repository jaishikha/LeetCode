from math import gcd

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        return gcd(min(nums), max(nums))

        #Euclidean Algorithm
        #def gcd(self, a, b):
        #while b:
            #a, b = b, a % b

        #return a