class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = {}
        maxLen = 0
        maxFreq = 0

        l, r = 0, 0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r], 0) + 1

            maxFreq = max(maxFreq, map[s[r]])

            windowLen = r - l + 1

            if (windowLen - maxFreq <= k):
                maxLen = max(maxLen, windowLen)
            else:
                map[s[l]] = map[s[l]] - 1
                l += 1

        return maxLen            
        