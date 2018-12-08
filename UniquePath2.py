
#https://leetcode.com/problems/unique-paths-ii/
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 
        rowSize = len(obstacleGrid)
        colSize = len(obstacleGrid[0])
        
        #if rowSize == 1 and colSize == 1:
        #    return 0
        
        def check(row, col, grid):
            return row < rowSize and col < colSize
        
        def isValidBox(row, col, grid):
            return grid[row][col] == 0
        
        def helper(row, col, memo, grid):
            
            if not isValidBox(row, col, grid):
                return 0
            
            if (row, col) in memo:
                return memo[(row,col)]
            right,down, totalWays = 0 , 0, 0
            if check(row + 1, col, grid):
                right = helper(row + 1, col, memo, grid)
                
            if check(row, col + 1, grid):
                down = helper(row, col + 1, memo, grid)  
                
            if row == rowSize - 1 and col == colSize - 1:
                totalWays = 1 
            
            totalWays = right + down + totalWays
            memo[(row, col)] = totalWays 
            return totalWays
        memo = {}
        return helper(0,0, memo, obstacleGrid)
            
