# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:11:48 2019

@author: Evan_He
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)  #可以反之从下往上
        for i in range(1,n):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1,i):
                triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
        return min(triangle[-1])