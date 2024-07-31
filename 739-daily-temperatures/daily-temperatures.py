class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Need to calculate diff if next element > el in stack
        # Need to store element and index

        res = [0]  * len(temperatures)
        stack=[] # temp and index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, index = stack.pop()
                res[index] = i - index

            stack.append((temp, i))

        return res         



        