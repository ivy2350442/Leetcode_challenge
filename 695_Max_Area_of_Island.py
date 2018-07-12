class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def dfs(i, j):
            if len(grid) > i >= 0 and len(grid[0]) > j >= 0 and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            else:
                return 0

        max_land = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #注意 if for 中不可存在遞迴 或 def
                temp = dfs(i, j)
                if max_land < temp:
                    max_land = temp

        return max_land
