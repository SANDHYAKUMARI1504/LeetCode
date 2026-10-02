class Solution:
    def countMentions(self, numberOfUsers, events):
        mentions = [0] * numberOfUsers
        online_again = [0] * numberOfUsers

        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == "OFFLINE" else 1))

        for event in events:
            event_type = event[0]
            time = int(event[1])
            data = event[2]

            if event_type == "OFFLINE":
                user = int(data)
                online_again[user] = time + 60

            else:
                if data == "ALL":
                    for i in range(numberOfUsers):
                        mentions[i] += 1

                elif data == "HERE":
                    for i in range(numberOfUsers):
                        if online_again[i] <= time:
                            mentions[i] += 1

                else:
                    for token in data.split():
                        user = int(token[2:])
                        mentions[user] += 1

        return mentions