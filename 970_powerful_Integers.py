# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 18:21:49 2019

@author: Evan_He
"""

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if x < y:
            x,y = y,x
        if x == 1:
            if bound >= 2:
                return [2]
            else:
                return []
        if y == 1:
            res = []
            i = 0
            t = x**i+1
            while t<bound:
                res.append(t)
                i += 1
                t = x**i+1
            return res 
        res = set()
        i = 0
        while True:
            t1 = x ** i 
            if t1 > bound:
                break
            j = 0
            while True:
                t2 = y ** j
                t = t1 + t2
                if t > bound:
                    break
                res.add(t)
                j += 1
            i += 1
        return list(res)