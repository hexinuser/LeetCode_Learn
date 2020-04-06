# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:06:57 2019

@author: Evan_He
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        up,down = 0,len(matrix)
        if down == 0:
            return []
        left,right = 0,len(matrix[0])
        if right == 0:
            return []
        while left< right and up < down:
            for i in range(left,right):
                res.append(matrix[up][i])
            for j in range(up+1,down):
                res.append(matrix[j][right-1])
            if left+1==right or up+1==down:
                break
            for i in range(right-2,left-1,-1):
                res.append(matrix[down-1][i])
            for j in range(down-2,up,-1):
                res.append(matrix[j][left])
            left += 1
            right -= 1
            up += 1
            down -= 1 
        return res
            