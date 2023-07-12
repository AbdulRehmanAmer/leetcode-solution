# My LeetCode Submission: https://leetcode.com/problems/decode-the-message/solutions/3753692/linear-time-solution-python-easiest-solution/
class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        # decoder = dict()
        secret_message = dict() # Reverse Mapping of Decoder

        look_up = ""

        alpha = 97
        for x in key:
            if x not in look_up and x != ' ': 
                secret_message[x] = chr(alpha)
                look_up += x
                alpha += 1
  
        # Time to decode the secret message
        ans = ""
        for x in message:
            if x == ' ': ans += x
            else: ans += secret_message[x]
        
        return ans


