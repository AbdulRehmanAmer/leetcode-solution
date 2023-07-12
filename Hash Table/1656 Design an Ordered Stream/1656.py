# My LeetCode Submission: https://leetcode.com/problems/design-an-ordered-stream/solutions/3753599/python-easiest-solution-linear-time-solution/
class OrderedStream:

    def __init__(self, n: int):
        self.hash_table = [None] * n
        self.ptr = 0
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.hash_table[idKey - 1] = value
        
        chunk = list()

        while self.ptr < len(self.hash_table) and self.hash_table[self.ptr] != None:
            if self.hash_table[self.ptr] == None: break
            chunk.append(self.hash_table[self.ptr])
            self.ptr += 1


        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)