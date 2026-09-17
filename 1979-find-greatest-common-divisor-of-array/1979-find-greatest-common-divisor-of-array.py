class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)

        while maxi != 0:
            mini, maxi = maxi, mini % maxi
        
        return mini
        