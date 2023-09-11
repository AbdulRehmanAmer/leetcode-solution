class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        prefix = ""
        for i in range(len(s[0])):
            flag = True
            for j in range(1, len(s)):
                    
                if i >= len(s[j]) or s[j][i] != s[0][i]: 
                    flag = not flag
                    break
            if flag:
                prefix += s[0][i]
            else:
                break
        return prefix
