class Solution(object):
    def numIslands(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numIslands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r, c) in visited:
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    numIslands += 1
                    dfs(r, c)

        return numIslands            


                

        