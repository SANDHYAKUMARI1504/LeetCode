class Solution:
    def averageWaitingTime(self, customers):
        current_time = 0
        total_waiting = 0

        for arrival, time in customers:
            current_time = max(current_time, arrival)
            current_time += time
            total_waiting += current_time - arrival

        return total_waiting / len(customers)