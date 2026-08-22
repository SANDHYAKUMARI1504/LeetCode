class Solution:
    def shortestSubstrings(self, arr):
        count = {}

        for s in arr:
            seen = set()

            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    seen.add(s[i:j])

            for sub in seen:
                count[sub] = count.get(sub, 0) + 1

        answer = []

        for s in arr:
            best = ""

            for i in range(len(s)):
                for j in range(i + 1, len(s) + 1):
                    sub = s[i:j]

                    if count[sub] == 1:
                        if (not best or
                            len(sub) < len(best) or
                            (len(sub) == len(best) and sub < best)):
                            best = sub

            answer.append(best)

        return answer