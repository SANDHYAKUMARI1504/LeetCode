from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d = {}

        for i, v in nums1:
            d[i] = d.get(i, 0) + v

        for i, v in nums2:
            d[i] = d.get(i, 0) + v

        return [[i, d[i]] for i in sorted(d)]
                
        