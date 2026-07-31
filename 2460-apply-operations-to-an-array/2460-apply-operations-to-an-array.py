from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        out = []

        for x in nums:
            if x != 0:
                out.append(x)

        while len(out) < len(nums):
            out.append(0)

        return out
        