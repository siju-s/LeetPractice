class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        res = 0
        l = 0

        # Maintain queues for O(1) access to min and max
        max_q = deque() # mono decreasing 
        min_q = deque() # mono increasing

        for r in range(len(nums)):

           while max_q and nums[r] > max_q[-1]:
                max_q.pop()

           while min_q and nums[r] < min_q[-1]:
                min_q.pop()  

           min_q.append(nums[r])
           max_q.append(nums[r])

           while max_q[0] - min_q[0] > limit:
                if nums[l] == max_q[0]:
                    max_q.popleft()

                if nums[l] == min_q[0]:
                    min_q.popleft()
                
                l += 1

           res = max(res, r - l + 1)

        return res     