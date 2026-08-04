class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0

        for i in words:
            consistent = True

            for ch in i:
                if ch not in allowed:
                    consistent = False
                    break

            if consistent:
                count += 1

        return count