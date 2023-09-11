class Solution:
    def maxArea(self, height) -> int:
        monotonic_stack = [[len(height) - 1, height[-1]]]
        for i in range (len(height) - 2, -1, -1):
           if height[i] > monotonic_stack[-1][1]: monotonic_stack.append( [i, height[i]] )

        area = float('-inf')
        for i in range(len(height)):
            j = 0
            while j < len(monotonic_stack) and monotonic_stack[j][1] < height[i]: 
                area = max(area, min(height[i], monotonic_stack[j][1]) * (monotonic_stack[j][0] - i))
                j += 1
            if j == len(monotonic_stack): continue;
            area = max(area, height[i] * (monotonic_stack[j][0] - i))
        return area
    

sol = Solution()
print (sol.maxArea([1,8,6,2,5,4,8,3,7]))
# print (sol.maxArea([2,3,4,5,18,17,6]))
# print (sol.maxArea([1,2,3,4,5,25,24,3,4]))