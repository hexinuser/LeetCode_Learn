# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:32:20 2018

@author: Evan_He
"""

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import numpy as np
        grid = np.array(grid)
        t1=sum(sum(grid))
        c_max=grid.max(axis=0) #列最大值
        r_max=grid.max(axis=1)
        m,n=grid.shape
        for i in range(m):
            for j in range(n):
                grid[i,j]=int(min(r_max[i],c_max[j]))
        return int(sum(sum(grid))-t1)
        
        