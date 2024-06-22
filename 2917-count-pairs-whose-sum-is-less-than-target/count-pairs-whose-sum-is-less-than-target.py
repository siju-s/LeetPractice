class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        for i, num in enumerate(nums):
            for num2 in nums[i + 1: len(nums)]:
                if num + num2 < target:
                    count += 1

        return count
                
        