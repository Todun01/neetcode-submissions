class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        water = 0
        while l < r:
            maxL, maxR = max(height[l], maxL), max(height[r], maxR)
            if height[l] > height[r]:
                if maxR - height[r] > 0:
                    water += (maxR - height[r])
                r -= 1
            else:
                if maxL - height[l] > 0:
                    water += (maxL - height[l])
                l += 1
        return water