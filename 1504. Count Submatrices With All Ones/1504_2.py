class Solution:
    def numSubmat(self, mat) -> int:
        res = 0
        for col_limit in range(1, len(mat[0]) + 1):
            for c in range(len(mat[0]) - col_limit + 1):
                length = 1
                for r in range(len(mat)):
                    sub_mat = mat[r][c : c + col_limit]
                    if 0 not in sub_mat:
                        res += length
                        length += 1
                    else:
                        length = 1
                
        
        return res
    
    # Rows are determined at the time of insertion in stack. 
    # Whenever a new column adds it should contain 1 in its whole set, and maintain m * n accordingly.
    # Also, we are adding into the `res` according to the factorial sum pattern. Like 3+2+1