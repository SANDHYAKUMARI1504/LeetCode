class Solution:
    def gridGame(self, grid):
        n = len(grid[0])

        top_remaining = sum(grid[0])

        bottom_remaining = 0

        answer = float('inf')

        for i in range(n):
 
            top_remaining -= grid[0][i]

            second_robot = max(top_remaining, bottom_remaining)

            answer = min(answer, second_robot)

            bottom_remaining += grid[1][i]

        return answer