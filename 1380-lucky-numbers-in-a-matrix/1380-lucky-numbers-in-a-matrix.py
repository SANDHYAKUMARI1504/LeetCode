class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        out = []

        for i in range(len(matrix)):
            row_min = min(matrix[i])

            for j in range(len(matrix[0])):
                col_max = max(matrix[k][j] for k in range(len(matrix)))

                if row_min == col_max:
                    out.append(row_min)

        return out