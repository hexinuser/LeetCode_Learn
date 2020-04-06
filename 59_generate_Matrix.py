# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 16:49:56 2018

@author: Evan_He
"""

class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        res =[[0]*n for _ in range(n)]
        left, right = 0, n-1
        i , j, k = 0, 0, 1
        while left <= n//2:
            while j < right:
                res[i][j] = k
                k += 1
                j += 1
            while i < right:
                res[i][j] = k
                k += 1
                i += 1
            right -= 1
            while j > left:
                res[i][j] = k
                k += 1
                j -= 1
            while i > left:
                res[i][j] = k
                k += 1
                i -= 1
            i += 1
            j += 1
            left += 1
        if n%2==1:
            res[i-1][j-1]=k
        return res