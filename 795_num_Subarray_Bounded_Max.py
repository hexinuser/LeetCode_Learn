# -*- coding: utf-8 -*-
"""
Created on Thu May  9 13:56:35 2019

@author: Evan_He
"""
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        res,k,ind = 0, -1, -1
        for i in range(len(A)):
            if A[i] > R:
                if ind !=-1:
                    res += (ind-k)*(i-ind)
                    ind = -1
                k = i
            elif A[i] >= L:
                if ind !=-1:
                    res += (ind-k)*(i-ind)
                ind = i   
        if k < ind:
            res += (ind-k)*(i+1-ind)
        return res
                