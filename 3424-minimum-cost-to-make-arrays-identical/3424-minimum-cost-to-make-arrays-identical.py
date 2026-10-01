class Solution:
    def minCost(self, arr, brr, k):

        cost1 = sum(abs(a - b) for a, b in zip(arr, brr))

        a = sorted(arr)
        b = sorted(brr)

        cost2 = k + sum(abs(x - y) for x, y in zip(a, b))

        return min(cost1, cost2)