class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ''
        temp = ''
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                if not ans: ans += temp
                elif temp: ans += ' ' + temp
                temp = ''
            else:
                temp = s[i] + temp
        if not ans and temp:
            return temp
        return ans + ' ' + temp if temp else ans