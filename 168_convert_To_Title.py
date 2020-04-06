# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:03:48 2019

@author: Evan_He
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            t = n%26
            if t == 0:
                res = 'Z'+res
                n = (n-26)//26
            else:
                res = chr(t+64)+res
                n = (n-t)//26
        return res