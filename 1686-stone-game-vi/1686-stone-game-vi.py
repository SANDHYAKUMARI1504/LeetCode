class Solution:
    def stoneGameVI(self, aliceValues, bobValues):
        n = len(aliceValues)

        stones = []

        for i in range(n):
            stones.append((aliceValues[i] + bobValues[i], i))

        stones.sort(reverse=True)

        alice = 0
        bob = 0

        for turn in range(n):
            i = stones[turn][1]

            if turn % 2 == 0:
                alice += aliceValues[i]
            else:
                bob += bobValues[i]

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0