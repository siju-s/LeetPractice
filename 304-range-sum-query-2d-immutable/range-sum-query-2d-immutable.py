class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + self.dp[r] [c + 1] + matrix[r][c] - self.dp[r][c]
          
        

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.dp[r2 + 1][c2 + 1] + self.dp[r1][c1] - self.dp[r1][c2 + 1] - self.dp[r2 + 1][c1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)