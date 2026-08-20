class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        ans = 0
        exchange = numExchange

        while full > 0:
            ans += full
            empty += full
            full = 0

            while empty >= exchange:
                empty -= exchange
                full += 1
                exchange += 1

        return ans