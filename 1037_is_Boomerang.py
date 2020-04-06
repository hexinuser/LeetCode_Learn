# -*- coding: utf-8 -*-
"""
Created on Tue May  7 22:23:10 2019

@author: Evan_He
"""

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0] * (points[1][1] - points[2][1]) + 
                points[1][0] * (points[2][1] - points[0][1]) + 
                points[2][0] * (points[0][1] - points[1][1])) != 0
        #判断三角形面积