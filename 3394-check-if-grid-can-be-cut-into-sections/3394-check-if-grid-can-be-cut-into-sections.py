from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def has_two_gaps(intervals: List[tuple]) -> bool:
            intervals.sort()
            gaps = 0
            cur_end = intervals[0][1]
            for start, end in intervals[1:]:
                if start >= cur_end:
                    gaps += 1
                    if gaps == 2:
                        return True
                cur_end = max(cur_end, end)
            return False

        x_intervals = [(x1, x2) for x1, _, x2, _ in rectangles]
        y_intervals = [(y1, y2) for _, y1, _, y2 in rectangles]

        return has_two_gaps(x_intervals) or has_two_gaps(y_intervals)