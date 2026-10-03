class Solution:
    def maxFreeTime(self, eventTime, startTime, endTime):
        n = len(startTime)

        gap = [0] * (n + 1)

        gap[0] = startTime[0]

        for i in range(1, n):
            gap[i] = startTime[i] - endTime[i - 1]

        gap[n] = eventTime - endTime[n - 1]

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)

        prefix[0] = gap[0]
        for i in range(1, n + 1):
            prefix[i] = max(prefix[i - 1], gap[i])

        suffix[n] = gap[n]
        for i in range(n - 1, -1, -1):
            suffix[i] = max(suffix[i + 1], gap[i])

        ans = 0

        for i in range(n):
            duration = endTime[i] - startTime[i]

            merged = gap[i] + duration + gap[i + 1]

            max_other_gap = 0

            if i - 1 >= 0:
                max_other_gap = max(max_other_gap, prefix[i - 1])

            if i + 2 <= n:
                max_other_gap = max(max_other_gap, suffix[i + 2])

            if max_other_gap >= duration:
                ans = max(ans, merged)
            else:
                ans = max(ans, merged - duration)

        return ans