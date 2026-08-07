class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        count = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                
                    row_sum = sum(mat[i])
                    
                    col_sum = 0
                    for k in range(m):
                        col_sum += mat[k][j]

                    if row_sum == 1 and col_sum == 1:
                        count += 1

        return count            
                   