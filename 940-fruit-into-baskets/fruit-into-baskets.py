class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxLen = 0
        l = 0
        limit = 2

       # Cant use a set because we cant remove all entries of that fruit 
        values = {}

        for r in range(len(fruits)):
            values[fruits[r]] = values.get(fruits[r], 0) + 1

            while len(values) > limit:
                values[fruits[l]] -= 1
                if values[fruits[l]] == 0:
                    del values[fruits[l]]
                l += 1

            maxLen = max(maxLen, r - l + 1)

        return maxLen             
        