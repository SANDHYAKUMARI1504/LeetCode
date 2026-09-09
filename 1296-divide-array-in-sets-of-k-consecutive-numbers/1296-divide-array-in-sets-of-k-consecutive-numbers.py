from collections import Counter

class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False

        count = Counter(nums)

        for x in sorted(count):
            if count[x] == 0:
                continue

            freq = count[x]

            for num in range(x, x + k):
                if count[num] < freq:
                    return False

                count[num] -= freq

        return True
        