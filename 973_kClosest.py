# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:00:55 2019

@author: Evan_He
"""

class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        def dist(t):
            return t[0]**2+t[1]**2
        points = [(point,dist(point)) for point in points]
        
        sort_res = sorted(points,key=lambda x: x[1])[:K]
        
        res = [res_i[0] for res_i in sort_res]
        return res