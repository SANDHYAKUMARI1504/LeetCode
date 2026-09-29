from collections import defaultdict

class Solution:
    def tupleSameProduct(self, nums):
        count = defaultdict(int)
        ans = 0

        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]

                ans += count[product] * 8

                count[product] += 1

        return ans