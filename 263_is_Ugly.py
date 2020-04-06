# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:10:00 2018

@author: Evan_He
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        if num%2==0 or num%3==0 or num%5==0:
            if num%2==0:
                num = num//2
            if num%3==0:
                num = num//3
            if num%5==0:
                num = num//5
            return self.isUgly(num)
        else:
            return  False