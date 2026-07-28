class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = "aeiouAEIOU"
        hasVowel = False
        hasConsonant = False

        for ch in word:
            # Invalid character
            if not (ch.isalpha() or ch.isdigit()):
                return False

            # Check vowels and consonants
            if ch.isalpha():
                if ch in vowels:
                    hasVowel = True
                else:
                    hasConsonant = True

        return hasVowel and hasConsonant
        