class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for x in s:
            if x.isalnum(): palindrome += x.lower()
        
        return True if palindrome == palindrome[::-1] else False
        