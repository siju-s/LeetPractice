class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = float('-inf')
        currentSum = 0
        for r in range(len(nums)):
            currentSum += nums[r]

            if r + 1 >= k:
                maxSum = max(maxSum, currentSum)
                currentSum -= nums[r - k + 1]

        return maxSum/k           

        