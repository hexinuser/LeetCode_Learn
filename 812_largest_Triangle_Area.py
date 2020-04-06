# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:52:12 2019

@author: Evan_He
"""

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def area(x,y,z):
            return abs(0.5*(x[0]*y[1]-y[0]*x[1]+y[0]*z[1]-z[0]*y[1]+z[0]*x[1]-x[0]*z[1]))
        res = area(points[0],points[1],points[2])
        n = len(points)
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    res = max(res,area(points[i],points[j],points[k]))
        return res