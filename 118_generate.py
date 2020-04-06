# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:45:54 2018

@author: Evan_He
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows ==0:
            return []
        result = [[1]]
        if numRows == 1:
            return result
        for i in range(2,numRows+1):
            m = i//2
            if i%2==0:
                row_i = [1]+[result[-1][t]+result[-1][t+1] for t in range(m-1)]
                row_i += row_i[::-1]
            else:
                row_i = [1]+[result[-1][t]+result[-1][t+1] for t in range(m-1)]
                row_i = row_i+[result[-1][m-1]+result[-1][m]] + row_i[::-1]
            result.append(row_i)
        return result