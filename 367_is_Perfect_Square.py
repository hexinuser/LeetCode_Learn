# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:27:59 2018

@author: Evan_He
"""

class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = 0
        b = num
        if num == 0:
            return True
        while True:
            t =(a+b)//2
            if t**2 == num:
                return True
            
            elif t**2<num:
                if (t+1)**2>num:
                    return False
                else:
                    a = t+1
            else:
                b = t