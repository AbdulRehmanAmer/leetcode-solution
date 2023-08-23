# My LeetCode Submission: https://leetcode.com/problems/unique-morse-code-words/solutions/3753735/python-easiest-solution-hash-table-solution-linear-time-solution/
class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        transformation = set()
        for word in words:
            s = ""
            for x in word:
                s += morse_code[ord(x) % 97]
            transformation.add(s)
        return len(transformation)