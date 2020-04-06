# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:22:04 2018

@author: Evan_He
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m , n = len(nums),len(nums[0])
        if m*n != r*c:
            return nums
        res = []
        i = j = 0
        for k1 in range(r):
            row = []
            for k2 in range(c):
                row.append(nums[i][j])
                j += 1
                if j == n:
                    i += 1
                    j = 0
            res.append(row)
        return res