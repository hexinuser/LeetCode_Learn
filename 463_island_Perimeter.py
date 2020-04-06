# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:03:37 2018

@author: Evan_He
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count=0
        count0=0
        m=len(grid)
        n=len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    count+=1
                    if i<m-1 and grid[i+1][j]==1:
                        count0+=1
                    if j<n-1 and grid[i][j+1]==1:
                        count0+=1    
        return count*4-2*count0