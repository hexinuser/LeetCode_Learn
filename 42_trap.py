# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:29:35 2019

@author: Evan_He
"""

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0
        res = 0
        i,j = 0,len(height)-1
        h0 = 0
        while i < j:
            if height[i] > h0 and height[j] > h0:
                if height[i] <= height[j]:
                    h1 = height[i]
                    i += 1
                else:
                    h1 = height[j]
                    j -= 1
                res += (j-i+2)*(h1-h0)
                h0 = h1
            if height[i] <= h0:
                i += 1
            if height[j] <= h0:
                j -= 1
        return res - sum(height)+max(height)-h0
                    
        """ 从左到右和从右到左填充之前的最大值，+所有元素的即为矩阵面积+雨水面积
        h1,h2 = 0,0
        res,n = 0,len(height)
        for i in range(0,n):
            h1 = max(height[i] , h1)
            h2 = max(height[-i-1] , h2)
            res += h1+h2-height
        return res - n*h1  
        """
        
       