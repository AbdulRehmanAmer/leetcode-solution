# My LeetCode Submission:https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/solutions/3754007/python-concise-easiest-solution/
class Solution:
    def maximumTime(self, time: str) -> str:
        if time[0] == "?": 
            if time[1] == "?" or int(time[1]) < 4:
                time = '2' + time[1 : ]
            else:
                time = '1' + time[1 : ]

        for i in range(1, len(time)):
            if time[i] == "?":
                part1, part2 = time[ : i], time[i + 1 : ]

                if i == 1:
                    if time[0] == "2":
                        time = part1 + "3" + part2
                    else:
                        time = part1 + '9' + part2
                elif i == 3:
                    time = part1 + "5" + part2
                else:
                    time = part1 + "9" + part2

        return time