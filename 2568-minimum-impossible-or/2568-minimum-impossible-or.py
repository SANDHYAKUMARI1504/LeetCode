class Solution:
    def minImpossibleOR(self, nums):
        s = set(nums)

        x = 1

        while x in s:
            x *= 2

        return x