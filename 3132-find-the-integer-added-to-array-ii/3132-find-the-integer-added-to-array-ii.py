from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        ans = float('inf')

        for i in range(3):
            x = nums2[0] - nums1[i]

            j = i + 1
            k = 1
            removed = 0

            while j < len(nums1) and k < len(nums2):
                if nums1[j] + x == nums2[k]:
                    j += 1
                    k += 1
                else:
                    removed += 1
                    j += 1

            removed += len(nums1) - j

            if k == len(nums2) and removed <= 2:
                ans = min(ans, x)

        return ans
        