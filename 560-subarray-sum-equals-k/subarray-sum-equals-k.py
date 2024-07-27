class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefixSum = 0
        # Store prefix Sum : frequency
        count = dict()
        count[0] = 1

        for num in nums:
            prefixSum += num
            # Adding frequency
            ans += count.get(prefixSum - k, 0)

            count[prefixSum] = count.get(prefixSum, 0) + 1


        return ans    

        