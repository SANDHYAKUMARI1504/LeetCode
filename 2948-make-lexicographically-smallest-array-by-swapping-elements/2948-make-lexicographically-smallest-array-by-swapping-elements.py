class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = [0] * len(nums)

        n = len(nums)
        start = 0

        while start < n:
            end = start

            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            indices = sorted(arr[k][1] for k in range(start, end + 1))

            for k, idx in enumerate(indices):
                ans[idx] = arr[start + k][0]

            start = end + 1

        return ans