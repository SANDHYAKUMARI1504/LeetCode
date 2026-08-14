from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        if k == 1:
            return n
        
        res = 0
        cnt = 1 
        
        for i in range(1, n + k - 1):
            if colors[i % n] != colors[(i - 1) % n]:
                cnt += 1
            else:
                cnt = 1
            
            if i >= k - 1 and cnt >= k:
                res += 1
        
        return res
        