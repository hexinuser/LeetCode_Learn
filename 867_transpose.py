# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:23:30 2018

@author: Evan_He
"""

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        B=[]
        for j in range(len(A[0])):
            B.append([A[i][j] for i in range(len(A))])
        return B
        """
        m,n=len(A),len(A[0])
        B = [[None] * m for _ in range(n)]
        for j in range(n):
            for i in range(m):
                B[j][i] = A[i][j]
        return B