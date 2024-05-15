class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     leftProdArr = [1] * len(nums)
    #     rightProdArr = [1] * len(nums)

    #     prod = 1
    #     for i in range(1, len(nums)):
    #         leftProdArr[i] = prod * nums[i - 1]
    #         prod = leftProdArr[i]

    #     prod = 1
    #     for j in range(len(nums) - 2, -1, -1):
    #         rightProdArr[j] = prod * nums[j + 1]
    #         prod = rightProdArr[j]

    #     output = [0] * len(nums)

    #     for i in range(0, len(nums)):
    #         output[i] = leftProdArr[i] * rightProdArr[i]

    #     return output    

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        leftProd = 1
        for i in range(len(nums)):
            output[i] *= leftProd
            leftProd *= nums[i] 

        rightProd = 1
        for j in range(len(nums) - 1, -1, -1):
            output[j] *= rightProd
            rightProd *= nums[j]


        return output    
        