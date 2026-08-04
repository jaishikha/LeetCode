class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = nums1 + nums2
        res.sort() 
        p = len(res)
        
        if p % 2 != 0:
            return float(res[p // 2])
        else:
            med1 = res[p // 2]
            med2 = res[(p//2) - 1]
            return (float(med1) + float(med2)) / 2

       