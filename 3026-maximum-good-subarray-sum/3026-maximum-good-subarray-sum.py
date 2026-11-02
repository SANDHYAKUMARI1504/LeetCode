class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        mp = {}
        ans = float('-inf')

        for x in nums:
            if x - k in mp:
                ans = max(ans, prefix + x - mp[x - k])

            if x + k in mp:
                ans = max(ans, prefix + x - mp[x + k])

            if x not in mp or prefix < mp[x]:
                mp[x] = prefix

            prefix += x

        return ans if ans != float('-inf') else 0