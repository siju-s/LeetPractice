class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()     

        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            start, end = i + 1, len(nums) - 1    

            while (start < end):
                num1 = nums[i]
                num2 = nums[start]
                num3 = nums[end]

                sum = num1 + num2 + num3

                if (sum == 0):
                    res.append([num1, num2, num3])
                    start += 1
                    end -= 1
                    while (start < end and nums[start] == nums[start - 1]):
                        start += 1

                elif (sum < 0):
                    start += 1
                else:
                    end -= 1        

            
        return res
        