# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 09:15:30 2019

@author: Evan_He
"""

class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if ops == []:
            return m*n
        """
        x_min_1 = min(ops,key = lambda x:x[0])[0] 
        x_min_2= min(ops,key = lambda x:x[1])[1]
        
        return x_min_1*x_min_2
        """
        import math
        x1 = math.inf
        x2 = math.inf
        for op in ops:
            if op[0] < x1:
                x1 = op[0]
            if op[1] < x2:
                x2 = op[1]
        return x1*x2