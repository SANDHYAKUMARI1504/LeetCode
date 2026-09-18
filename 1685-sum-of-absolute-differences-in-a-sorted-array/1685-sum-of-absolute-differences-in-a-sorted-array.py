class Solution:
    def getSumAbsoluteDifferences(self, nums):
        n = len(nums)
        total = sum(nums)
        result = []

        left_sum = 0

        for i in range(n):
            x = nums[i]

            left = x * i - left_sum

            right_sum = total - left_sum - x
            right_count = n - i - 1
            right = right_sum - x * right_count

            result.append(left + right)

            left_sum += x

        return result