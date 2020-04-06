# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:13:48 2019

@author: Evan_He
"""

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res = []
        t = 0
        for i in A:
            if i == 0:
                t *= 2
            else:
                t = t*2+1
            t = t%5
            res.append(t==0)
        return res