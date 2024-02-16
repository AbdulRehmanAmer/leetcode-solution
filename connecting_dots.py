class Solution:
    def __init__(self, matrix) -> None:
        self.res = 0
        self.matrix = matrix

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == 'Y':
                    self.res += 1
                    self.dfs(i, j, True)
        
    def dfs(self, i = 0, j = 0, flag = True): 
            if 0 <= i < len(self.matrix) and 0 <= j < len(self.matrix[i]):
                if self.matrix[i][j] == 'Y':
                    self.matrix[i][j] = '-'
                    self.dfs(i + 1, j, True)
                    self.dfs(i, j + 1, True)
        

if __name__ == "__main__":
    matrix = [
        ['Y','N','Y'],
        ['N','Y','N'],
        ['Y','N','Y'],
    ]


    res_matrix = [
        ['-','-','N'],
        ['-','N','-'],
        ['N','-','N'],
    ]

    sol = Solution(matrix)
    print (sol.res)
    print (sol.matrix)
