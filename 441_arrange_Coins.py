# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:44:59 2018

@author: Evan_He
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        #导出数学公式
        return int((2*n+0.25)**(0.5)-0.5)