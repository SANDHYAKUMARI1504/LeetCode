class Solution:
    def findDiagonalOrder(self, nums):
        diagonals = {}

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                d = i + j

                if d not in diagonals:
                    diagonals[d] = []

                diagonals[d].append(nums[i][j])

        ans = []

        for d in range(len(diagonals)):
            diagonals[d].reverse()
            ans.extend(diagonals[d])

        return ans