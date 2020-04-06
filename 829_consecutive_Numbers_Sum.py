# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:38:07 2019

@author: Evan_He
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 0 
        n = int((2*N+1/4)**0.5-0.5)
        for i in range(1,n+1):
            if (N-(i-1)*i//2)%i == 0:
                res += 1
        return res
    