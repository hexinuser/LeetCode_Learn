# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:43:42 2019

@author: Evan_He
"""

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        """return sorted([x**2 for x in A])"""
        res = []
        i,j = 0,len(A)-1
        while i <= j:
            if A[i]**2 >= A[j]**2:
                res.append(A[i]**2)
                i += 1
            else:
                res.append(A[j]**2)
                j -= 1
        res.reverse()
        return res