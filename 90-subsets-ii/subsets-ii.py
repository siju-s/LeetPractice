class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()

        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Backtrack and skip duplicates
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
                
            dfs(i + 1)

        dfs(0)
        return result    

        