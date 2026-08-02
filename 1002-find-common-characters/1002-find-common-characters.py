class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        out = []

        for ch in words[0]:
            found = True

            for i in range(1, len(words)):
                if ch in words[i]:
                    words[i] = words[i].replace(ch, "", 1)
                else:
                    found = False
                    break

            if found:
                out.append(ch)

        return out