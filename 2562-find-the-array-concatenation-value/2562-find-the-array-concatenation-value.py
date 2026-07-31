from typing import List

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        con = 0

        while len(nums) > 0:
            if len(nums) > 1:
                con += int(str(nums[0]) + str(nums[-1]))
                nums.pop()      
                nums.pop(0)     
            else:
                con += nums[0]
                nums.pop()

        return con

        