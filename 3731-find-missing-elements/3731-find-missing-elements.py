class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        seen = set(nums)
        for i in range(min(nums), max(nums)):
            if i not in seen:
                res.append(i)
            
        return res

