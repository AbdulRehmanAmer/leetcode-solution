# My Leetcode Submission: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/solutions/3791602/easiest-concise-simple-solution/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        string = collections.deque([x for x in s[ : 3]])
        if len(set(string)) == 3: ans = 1
        else: ans = 0

        for i in range(1, len(s) - 2):
            string.popleft()
            string.append(s[i + 2])
            if len (set(string)) == 3: ans += 1
        
        return ans
