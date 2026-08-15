class Solution:
    def findWinningPlayer(self, skills, k):
        n = len(skills)
        current = 0
        wins = 0
        for i in range(1, n):
            if skills[current] > skills[i]:
                wins += 1
            else:
                current = i
                wins = 1
            if wins >= k:
                return current
        return current