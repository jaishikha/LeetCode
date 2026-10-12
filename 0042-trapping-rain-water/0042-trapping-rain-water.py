class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1
        l_max = height[l]
        r_max = height[r]
        water = 0

        while l < r:
            if l_max < r_max:
                l += 1
                l_max = max(l_max, height[l])
                water += l_max - height[l]
            else:
                r -= 1
                r_max = max(r_max, height[r])
                water += r_max - height[r]

        return water