class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return "" 
        count_s = {}
        count_t = {}
        
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        resLen = float("infinity")
        l = 0
        res = [-1, 1]

        # Have is current number of unique elements, need is total num of unique elements needed
        have, need = 0, len(count_t)

        for r in range(len(s)):
            c = s[r]
            count_s[c] = 1 + count_s.get(c, 0)

            if c in count_t and count_s[c] == count_t[c]:
                have += 1


            while have == need:
                # Calculate min window
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                
                count_s[s[l]] -= 1
                # Check if count got reduced for this removed character
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                   have -= 1

                l += 1

        l, r = res
        return s[l:r + 1] if resLen != float("infinity") else ""                     