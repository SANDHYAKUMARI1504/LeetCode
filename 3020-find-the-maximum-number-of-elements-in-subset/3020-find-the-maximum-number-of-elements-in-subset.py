from collections import Counter

class Solution:
    def maximumLength(self, nums: list[int]) -> int:
        freq = Counter(nums)
        ans = 1

        if freq[1] > 0:
            ans = max(ans, freq[1] if freq[1] % 2 == 1 else freq[1] - 1)

        for x in freq:
            if x == 1:
                continue

            length = 0
            cur = x

            while cur != 1 and freq[cur] >= 2:
                length += 2
                cur = cur * cur

            if freq[cur] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
        