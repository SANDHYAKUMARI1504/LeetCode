class Solution:
    def averageWaitingTime(self, customers):
        t = total = 0

        for a, p in customers:
            if t < a:
                t = a
            t += p
            total += t - a

        return total / len(customers)