# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:05:30 2019

@author: Evan_He
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i,k = 0, n//2
        j1,j2 = 0,n-1
        while i < k:
            for j in range(0,j2-j1):
                matrix[j1][j1+j],matrix[j1+j][j2],matrix[j2][j2-j],matrix[j2-j][j1]=matrix[j2-j][j1],matrix[j1][j1+j],matrix[j1+j][j2],matrix[j2][j2-j]
            j1 += 1
            j2 -= 1
            i += 1