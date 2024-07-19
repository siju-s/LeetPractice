class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        currentSum = 0

        for r in range(len(arr)):
            currentSum += arr[r]
            if r + 1 >= k:
                if currentSum/k >= threshold:
                    count += 1
                currentSum -= arr[r - k + 1]

        return count        
                    

        