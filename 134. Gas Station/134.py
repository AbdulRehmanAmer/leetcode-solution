class Solution:
    def canCompleteCircuit(self, gas, cost) -> int:
        track = None
        for i in range(len(gas)):
            if gas[i] >= cost[i]: 
                if track == None:
                    track = i
                elif gas[track] > gas[i]:
                    track = i


        if track == None:
            return -1
        
        ans = track
        fuel = gas[track]
        isreach = 0
        for _ in range(len(gas)):
            temp = fuel - cost[track % len(gas)]
            if temp < 0: return -1
            track += 1
            fuel = temp + gas[track % len(gas)]
        return ans


sol = Solution()
res = sol.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2])
print (res)        
