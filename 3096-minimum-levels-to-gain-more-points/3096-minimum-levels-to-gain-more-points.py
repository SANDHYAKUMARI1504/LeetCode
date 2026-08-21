class Solution:
    def minimumLevels(self, possible):
        n = len(possible)

        score = [1 if x == 1 else -1 for x in possible]

        bob = sum(score)
        alice = 0

        for i in range(n - 1):
            alice += score[i]
            bob -= score[i]

            if alice > bob:
                return i + 1

        return -1
        