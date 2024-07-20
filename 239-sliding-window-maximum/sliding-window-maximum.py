class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        l = 0

        for r in range(len(nums)):
            num = nums[r]

            while q and num > nums[q[-1]]:
                q.pop()

            # Storing indices to allow us to pop the element if it falls outside the window
            q.append(r)

            #Check if max element(first element) no longer in window
            if l > q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1

        return res
        