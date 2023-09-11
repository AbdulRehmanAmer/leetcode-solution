from collections import deque
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        track = deque(["" for _ in range(numRows)])
        s = deque(s)
        while s:
            row = 0
            while s and row < numRows:
                track[row] += s.popleft()
                row += 1
            row = numRows - 2
            while s and row > 0:
                track[row] += s.popleft()
                row -= 1
        s = ""
        while track:
            s += track.popleft()
        return s

            
