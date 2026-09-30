class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twos = 0

        for num in nums:
            if num == 0:
                zeroes += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1

        i = 0
        while zeroes != 0:
            nums[i] = 0
            zeroes -= 1
            i += 1

        while ones != 0:
            nums[i] = 1
            ones -= 1
            i += 1

        while twos != 0:
            nums[i] = 2
            twos -= 1
            i += 1

        