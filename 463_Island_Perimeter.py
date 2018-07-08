class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        ans = 0
        for i in range(len(grid[0])):
            if grid[0][i] == 1:
                ans += 1
            for j in range(1, len(grid), 1):
                if grid[j][i] != grid[j-1][i]:
                    ans += 1
            if grid[len(grid)-1][i] == 1:
                ans += 1

        for i in range(len(grid)):
            if grid[i][0] == 1:
                ans += 1
            for j in range(1, len(grid[0]), 1):
                if grid[i][j] != grid[i][j-1]:
                    ans += 1
            if grid[i][len(grid[0])-1] == 1:
                ans += 1

        return ans
