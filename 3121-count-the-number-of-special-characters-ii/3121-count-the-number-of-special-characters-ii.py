class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        for c in "abcdefghijklmnopqrstuvwxyz":
            lower = c
            upper = c.upper()

            if lower in word and upper in word:
                first_upper = word.index(upper)
                last_lower = word.rfind(lower)

                if last_lower < first_upper:
                    count += 1

        return count