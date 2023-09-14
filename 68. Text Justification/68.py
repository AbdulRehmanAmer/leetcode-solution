from collections import deque
class Solution:
    def fullJustify(self, words, maxWidth: int):
        words = deque(words)
        ans = list()

        while words:
            temp = []
            current_width = 0

            while words:
                temp_word = words.popleft()
                if (not temp and len(temp_word) + current_width <= maxWidth) or (len(temp_word) + current_width + 1 <= maxWidth):
                    current_width += len(temp_word)
                    if temp:
                        temp[-1] += " "
                        current_width += 1
                    temp += [temp_word]
                else:
                    words.appendleft(temp_word)
                    break

            remaining_spaces = maxWidth % current_width
            if len(temp) != 1:
                add_spaces = remaining_spaces // (len(temp) - 1)

                for i in range(len(temp) - 1): # Confirmed spaces that need to be added evenly to each words
                    temp[i] += (" " * add_spaces)
                    
                left_justification = remaining_spaces % (len(temp) - 1) # If that number is not divisible, then its time for the left justification.
                for i in range(left_justification):
                    temp[i] += " "

            ans += ["".join(temp)]

        for i in range(len(ans) - 1):
            s = ans[i].split()
            if len(s) != 2:
                ans[i] += (" " * (maxWidth - len(ans[i])))
            else:
                count  = len(s[0]) + len(s[1])
                s = s[0] + (" " * (maxWidth - count)) + s[1]
                ans[i] = s
                
        last_phrase = " ".join(ans.pop().split())
        last_phrase += (" " * (maxWidth - len(last_phrase)))
        ans.append(last_phrase)
        
        return ans