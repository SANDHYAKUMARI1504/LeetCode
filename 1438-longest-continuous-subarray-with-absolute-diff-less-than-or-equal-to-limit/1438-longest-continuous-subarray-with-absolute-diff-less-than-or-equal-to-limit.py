from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):
        maxdq = deque()
        mindq = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            while maxdq and nums[maxdq[-1]] < nums[right]:
                maxdq.pop()

            maxdq.append(right)

            while mindq and nums[mindq[-1]] > nums[right]:
                mindq.pop()

            mindq.append(right)

            while nums[maxdq[0]] - nums[mindq[0]] > limit:

                if maxdq[0] == left:
                    maxdq.popleft()

                if mindq[0] == left:
                    mindq.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans