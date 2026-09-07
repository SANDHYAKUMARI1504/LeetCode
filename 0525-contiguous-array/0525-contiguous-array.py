class Solution:
    def findMaxLength(self, nums):
        first = {0: -1}   
        prefix_sum = 0
        max_len = 0

        for i, num in enumerate(nums):
            if num == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in first:
                max_len = max(max_len, i - first[prefix_sum])
            else:
                first[prefix_sum] = i

        return max_len