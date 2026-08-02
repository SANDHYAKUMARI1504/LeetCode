class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]):
        out = []
        extra = []

        for x in arr2:
            for y in arr1:
                if x == y:
                    out.append(y)

        for y in arr1:
            if y not in arr2:
                extra.append(y)

        extra.sort()

        return out + extra      