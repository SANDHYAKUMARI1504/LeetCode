class Solution:
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        mid = n // 2

        y = [0, 0, 0]
        other = [0, 0, 0]

        for r in range(n):
            for c in range(n):
                is_y = False

                if r <= mid and (c == r or c == n - 1 - r):
                    is_y = True

                if r >= mid and c == mid:
                    is_y = True

                if is_y:
                    y[grid[r][c]] += 1
                else:
                    other[grid[r][c]] += 1

        ans = float('inf')

        for y_val in range(3):
            for other_val in range(3):
                if y_val == other_val:
                    continue

                changes = (
                    sum(y) - y[y_val] +
                    sum(other) - other[other_val]
                )

                ans = min(ans, changes)

        return ans