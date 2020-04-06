# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:22:51 2019

@author: Evan_He
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        if n == 0:
            return False
        elif len(matrix[0]) == 0:
            return False
        row = [matrix[k][0] for k in range(n)]
        m1 = self.mid_sear(row,target)
        if row[m1] == target:
            return True
        m2 = self.mid_sear(matrix[m1],target)
        return matrix[m1][m2] == target
    
    def mid_sear(self,array,tar):
        i,j = 0,len(array)
        while i<j:
            mid = (i+j)//2
            if array[mid] == tar:
                return mid
            elif array[mid] > tar:
                j = mid
            else:
                if mid + 1 == j:
                    return mid
                elif array[mid+1] > tar:
                    return mid
                else:
                    i = mid + 1
        return mid