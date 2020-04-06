# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 20:14:01 2019

@author: Evan_He
"""

class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        t = 0
        for num in A:
            if num%2==0:
                t += num
        res = []
        for [val,index] in queries:
            if A[index]%2 == 0:
                if val%2 == 0:
                    t += val
                else:
                    t -= A[index]
            else:
                if val%2 == 1:
                    t += val+A[index]
            A[index] += val
            res.append(t)
        return res