class Solution:
    def numberOfMatches(self, n: int) -> int:
        team = n
        matches = 0

        while team > 1:
            if team % 2 == 0:
                match = team // 2
                team = team // 2
            else:
                match = (team - 1) // 2
                team = (team - 1) // 2 + 1

            matches += match

        return matches    

        