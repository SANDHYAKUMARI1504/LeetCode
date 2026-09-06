from collections import deque

class Solution:
    def highestPeak(self, isWater):
        m = len(isWater)
        n = len(isWater[0])

        height = [[-1] * n for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:
 
                    if height[nr][nc] == -1:
                        height[nr][nc] = height[r][c] + 1
                        q.append((nr, nc))

        return height