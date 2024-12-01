class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(index):
            if index == len(nums):
                print(f"Index: {index}, Subset: {subset}")
                res.append(subset.copy())
                return

            # include nums[i]
            subset.append(nums[index])
            dfs(index + 1)

            # do NOT include nums[i]
            subset.pop()
            dfs(index + 1)

        dfs(0)
        return res