# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:53:57 2019

@author: Evan_He
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i,j = 0,len(height)-1
        res = 0
        while i < j:
            if height[i] <= height[j]:
                t = (j-i)*height[i]
                i += 1
            else:
                t = (j-i)*height[j]
                j -= 1
            if t > res:
                res = t
        return res
            