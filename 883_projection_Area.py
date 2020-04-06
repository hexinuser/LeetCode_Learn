# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:56:52 2018

@author: Evan_He
"""

class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        n = len(grid)
        res = sum([max(t) for t in grid])
        for j in range(n):
            max_col_j = 0
            for i in range(n):
                if grid[i][j] > 0:
                    res += 1
                if grid[i][j]> max_col_j:
                    max_col_j = grid[i][j]
                    
            res += max_col_j
        return res
        """
        n = len(grid)
        res = n**2 - sum([t.count(0) for t in grid])
        res += sum([max(value) for value in grid])
        res += sum([max(value) for value in zip(*grid)])
        return res
    
    