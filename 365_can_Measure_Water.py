# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 00:35:04 2019

@author: Evan_He
"""

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if x > y:
            x,y = y,x
        if x+y < z:
            return False
        if x == y:
            if x == 0:
                return z == 0
            return z%x == 0
        if x == 0:
            return z%y == 0
        z = z%x
        if z == 0:
            return True
        for i in range(1,x):
            t = y*i%x
            if t == z or x-t == z:
                return True
        return False
    
        """#判断最大公约数
        if z == 0:
            return True
        if x+y < z:
            return False
        if x>y:
            x,y=y,x
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0
        """