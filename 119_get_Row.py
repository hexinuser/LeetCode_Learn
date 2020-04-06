# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:37:28 2018

@author: Evan_He
"""

class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        res = [1]
        res_row = self.getRow(rowIndex-1)
        for i in range(1,rowIndex):
            res.append(res_row[i-1]+res_row[i])
        res.append(1)
        return res