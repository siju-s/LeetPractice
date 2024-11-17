class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxLen = 0
        chars = set()
        left = 0

        for right in range(len(s)):
            while s[right] in chars:
                chars.remove(s[left])
                left += 1

            chars.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen    
        