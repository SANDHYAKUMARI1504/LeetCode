class Solution:
    def subarraysDivByK(self, nums, k):
        count = {0: 1}
        prefix = 0
        ans = 0

        for num in nums:
            prefix += num

            rem = prefix % k

            if rem in count:
                ans += count[rem]

            count[rem] = count.get(rem, 0) + 1

        return ans