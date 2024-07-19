class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        l = 0
        currentSum = 0

        for r in range(len(arr)):
            if r - l + 1 > k:
                currentSum -= arr[l]
                l += 1

            currentSum += arr[r]

            if r - l + 1 == k and currentSum/k >= threshold:
                count += 1

        return count        
                    

        