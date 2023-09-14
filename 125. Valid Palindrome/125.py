class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for x in s:
            if 48 <= ord(x) <= 48 + 9 or 97 <= ord(x.lower()) < 97 + 26: palindrome += x.lower()
        for i in range(len(palindrome) // 2):
            if palindrome[i] != palindrome[-1 - i]: return False
        return True
        
                