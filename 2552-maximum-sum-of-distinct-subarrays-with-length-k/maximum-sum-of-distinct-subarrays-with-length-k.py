class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Fixed sliding window
        # Keep track of current sum
        # Use set to check duplicates

        numSet = set()
        currentSum = 0
        maxSum = 0
        l, r = 0, 0

        while r < len(nums):
            while nums[r] in numSet:
                currentSum -= nums[l]
                numSet.remove(nums[l])
                l += 1
            currentSum += nums[r]
            numSet.add(nums[r])  
                
            if r - l + 1 == k:
                maxSum = max(maxSum, currentSum)
                currentSum -= nums[l]
                numSet.remove(nums[l])
                l += 1

            r += 1    


        return maxSum            

                     
        