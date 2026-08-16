from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        bad = [0] * n

        for i in range(1, n):
            bad[i] = bad[i - 1]

            if nums[i] % 2 == nums[i - 1] % 2:
                bad[i] += 1

        answer = []

        for l, r in queries:

            invalid_pairs = bad[r] - bad[l]

            if invalid_pairs == 0:
                answer.append(True)
            else:
                answer.append(False)

        return answer
        