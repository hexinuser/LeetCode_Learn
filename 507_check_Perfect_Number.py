# -*- coding: utf-8 -*-
"""
Created on Sat May  4 21:22:33 2019

@author: Evan_He
"""

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        res = 1
        n = int(num**0.5)
        for i in range(2,n+1):
            if num%i == 0:
                res += i+num//i
        if n**2 == num:
            res -= n
        return res==num
        