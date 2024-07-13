class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, 0
        totalSum = 0
        maxFreq = 0

        for r in range(len(nums)):
            totalSum += nums[r]

            while nums[r] * (r - l + 1) > totalSum + k:
                totalSum -= nums[l]
                l += 1 
                
        
            maxFreq = max(maxFreq, r - l + 1)


        return maxFreq    