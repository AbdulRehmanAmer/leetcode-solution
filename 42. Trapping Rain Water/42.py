class Solution:
    def trap(self, height) -> int:
        gap = [0] * len(height)

        max_left = height[0]
        for i in range(1, len(height)):
            if height[i] >= max_left:
                max_left = height[i]
                continue; 
            gap[i] = max_left - height[i]

        gap[-1] = 0
        max_right = height[-1]
        for i in range(len(height) - 2, -1, -1):
            if height[i] >= max_right:
                max_right = height[i]
            temp = max(max_right - height[i], 0)
            gap[i] = min(gap[i], temp)
        

                
        return sum(gap)

                