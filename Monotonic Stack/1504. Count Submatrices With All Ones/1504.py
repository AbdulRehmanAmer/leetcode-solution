class Solution:
    def numSubmat(self, mat) -> int:
        # After a lot of struggling
        res = 0
        for col_limit in range(1, len(mat[0]) + 1):
            for c in range(len(mat[0]) - col_limit + 1):
                stack = list()
                length = 1
                for r in range(len(mat)):
                    sub_mat = mat[r][c : c + col_limit]
                    if 0 not in sub_mat:
                        stack += [1] * length
                        length += 1
                    else:
                        res += len(stack)
                        stack = []
                        length = 1
                res += len(stack)
                
        
        return res
                        
        # Sturggling              
        # 1 * n
        # ans = 0
        # col_capacity = 1
        
        # while col_capacity <= len(mat[0]):
        #     flag = False
        #     for i in range(len(mat)):
                
        #         current_col_capacity = 1
        #         for j in range(len(mat[i])):
        #             if mat[i][j]:
        #                 if current_col_capacity == col_capacity: 
        #                     ans += 1
        #                     current_col_capacity = col_capacity - 1
        #                     flag = True
        #             elif not mat[i][j]: 
        #                 current_col_capacity = 0
        #             current_col_capacity += 1
        #     if not flag:
        #         break
        #     col_capacity += 1
        
        # n * 1
        # row_capacity = 2
        
        # while row_capacity <= len(mat):
        #     flag = False
        #     for j in range(len(mat[0])):
                
        #         current_row_capacity = 1
        #         for i in range(len(mat)):
        #             if mat[i][j]:
        #                 if current_row_capacity == row_capacity: 
        #                     ans += 1
        #                     current_row_capacity = row_capacity - 1
        #                     flag = True
                            
        #             elif not mat[i][j]: 
        #                 current_row_capacity = 0
        #             current_row_capacity += 1
        #     if not flag: break
        #     row_capacity += 1
         
        # n * n
        # for current_cols in range(1, len(mat[0]) + 1):
        #     for r in range(1, len(mat) + 2):
        #         ones_sub_mat = list()
        #         for c in range(len(mat[0]) - current_cols + 1):
        #             current_rows = 1
        #             for k in range(len(mat)):
        #                 if 0 not in mat[k][c : c + current_cols]:
        #                     if current_rows == r:
        #                         ones_sub_mat.append(1)
        #                         current_rows = r - 1
                                
        #                 if 0 in mat[k][c : c + current_cols]:
        #                     current_rows = 0
        #                 current_rows += 1
                        
        #         ans += len(ones_sub_mat)
            
        # return ans
    

    
sol = Solution()
print (sol.numSubmat([[1,0,1],[1,1,0],[1,1,0]]))
print (sol.numSubmat([[0,1,1,0],[0,1,1,1],[1,1,1,0]]))
print (sol.numSubmat([[1,1,1,1,1,1]]))