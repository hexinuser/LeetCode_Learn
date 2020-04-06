# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 16:53:47 2018

@author: Evan_He
"""

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n = len(A),len(A[0])
        for i in range(m):
            for j in range(n//2):
                A[i][j],A[i][n-1-j] = 1-A[i][n-1-j],1-A[i][j]
            if n % 2 == 1:
                A[i][n//2] = 1 - A[i][n//2]
        return A