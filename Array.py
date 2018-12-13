# https://leetcode.com/problems/minimum-path-sum/description/
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col ==0:
                    continue
                if row == 0:
                    grid[row][col] += grid[row][col-1]
                    print(grid[row][col])
                elif col == 0:
                    grid[row][col] += grid[row-1][col]
                    print(grid[row][col])
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                    print(grid[row][col])
        return grid[-1][-1]