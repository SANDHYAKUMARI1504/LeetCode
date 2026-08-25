class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = [0] * 26
        
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        mx = max(freq)
        
        ans = []
        for i in range(len(s) - 1, -1, -1):
            idx = ord(s[i]) - ord('a')
            
            if freq[idx] == mx:
                ans.append(s[i])
                freq[idx] = 0
        
        return ''.join(reversed(ans))