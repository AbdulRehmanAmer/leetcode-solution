class Solution:
    def trap(self, height) -> int:
        i = 0
        while i < len(height) and height[i] == 0: i += 1
        if i == len(height): return 0

        monotonic_stack = [height[i]]
        trapped_water = 0
        for i in range(i + 1, len(height)):
            if height[i] < monotonic_stack[-1]: monotonic_stack.append(height[i])
            else:
                n = min(monotonic_stack[0], height[i])
                for j in range(1, len(monotonic_stack)):
                    
                    trapped_water += max(n - monotonic_stack[j], 0)
                    monotonic_stack[j] = max(monotonic_stack[j], n)
                    if monotonic_stack[j] > n: break


                if n == monotonic_stack[0]: monotonic_stack = []
                monotonic_stack.append(height[i])
        return trapped_water
                
                    

sol = Solution()
n = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print (n)