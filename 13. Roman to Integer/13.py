class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        i = 0
        while i < len(s):
            if s[i] == "I":
                if i + 1 < len(s) and s[i + 1] == "V":
                    number += 4
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "X":
                    number += 9
                    i += 1
                else:
                    number += hashmap[s[i]]
            elif s[i] == "X":
                if i + 1 < len(s) and s[i + 1] == "L":
                    number += 40
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "C":
                    number += 90
                    i += 1
                else:
                    number += hashmap[s[i]]
            elif s[i] == "C":
                if i + 1 < len(s) and s[i + 1] == "D":
                    number += 400
                    i += 1
                elif i + 1 < len(s) and s[i + 1] == "M":
                    number += 900
                    i += 1
                else:
                    number += hashmap[s[i]]
            else:
                number += hashmap[s[i]]
            
            i += 1
            
        return number
sol = Solution()
# n = sol.romanToInt("III")
# n = sol.romanToInt("LVIII")
# n = sol.romanToInt("CI")
n = sol.romanToInt("MCDLXXVI")
print (n)