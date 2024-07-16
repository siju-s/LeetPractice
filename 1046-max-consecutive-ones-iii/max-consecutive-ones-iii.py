class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        numZeros = 0
        maxLen = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZeros += 1

            if numZeros > k:
                if nums[l] == 0:
                    numZeros -= 1
                l += 1
            if numZeros <= k:
                maxLen = max(maxLen, r - l + 1)

        return maxLen        

        