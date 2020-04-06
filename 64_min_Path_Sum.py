# -*- coding: utf-8 -*-
"""
Created on Fri May  3 14:25:56 2019

@author: Evan_He
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
        
        """
        m,n = len(grid),len(grid[0])
        if m*n == 1:
            return grid[0][0]
        elif m == 1:
            return grid[0][0]+self.minPathSum(grid[:][1:])
        elif n == 1:
            return grid[0][0]+self.minPathSum(grid[1:][:])
        else:
            return grid[0][0]+min(self.minPathSum(grid[:][1:]),self.minPathSum(grid[1:][:]))
        """