class Solution:
    def resultGrid(self, image, threshold):
        m, n = len(image), len(image[0])

        total = [[0] * n for _ in range(m)]
        count = [[0] * n for _ in range(m)]

        # Horizontal valid edges
        h = [[False] * (n - 1) for _ in range(m)]
        for i in range(m):
            for j in range(n - 1):
                h[i][j] = abs(image[i][j] - image[i][j + 1]) <= threshold

        # Vertical valid edges
        v = [[False] * n for _ in range(m - 1)]
        for i in range(m - 1):
            for j in range(n):
                v[i][j] = abs(image[i][j] - image[i + 1][j]) <= threshold

        for i in range(m - 2):
            for j in range(n - 2):

                valid = True

                # 6 horizontal edges
                for r in range(i, i + 3):
                    if not h[r][j] or not h[r][j + 1]:
                        valid = False
                        break

                # 6 vertical edges
                if valid:
                    for r in range(i, i + 2):
                        if not v[r][j] or not v[r][j + 1] or not v[r][j + 2]:
                            valid = False
                            break

                if not valid:
                    continue

                # Calculate region sum
                s = 0
                for r in range(i, i + 3):
                    s += image[r][j] + image[r][j + 1] + image[r][j + 2]

                avg = s // 9

                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        total[r][c] += avg
                        count[r][c] += 1

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if count[i][j]:
                    result[i][j] = total[i][j] // count[i][j]
                else:
                    result[i][j] = image[i][j]

        return result