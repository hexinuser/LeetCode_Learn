# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:44:54 2018

@author: Evan_He
"""

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m-1):
            for j in range(n-1):
                if matrix[i][j]!=matrix[i+1][j+1]:
                    return False
        return True
        """
        m = len(matrix)
        for i in range(m-1):
            if  matrix[i][:-1]!=matrix[i+1][1:]:
                return False
        return True
