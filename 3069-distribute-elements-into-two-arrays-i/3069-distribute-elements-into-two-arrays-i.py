class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr1 = []
        arr2 = []
        res = []
        for i in range(n-1):
            if i % 2 == 0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
            
        if arr1[-1] > arr2[-1]:
            arr1.append(nums[-1])
        else:
            arr2.append(nums[-1])

        res= arr1 + arr2

        return res