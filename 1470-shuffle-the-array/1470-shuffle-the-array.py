class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [] 
        j = n

        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[j])
            j += 1

        return ans