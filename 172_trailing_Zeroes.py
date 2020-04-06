# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:39:47 2019

@author: Evan_He
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        res = 0
        k = 1
        while n >= 5**k:
            res += n//(5**k)
            k += 1
        return res