# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:33:59 2018

@author: Evan_He
"""
class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        num = bin(N)[2:]
        res = 0
        index0 = num.find('1')
        index1 = num.find('1',index0+1)
        while index1 != -1:
            res = max(index1 - index0,res)
            index0,index1 = index1,num.find('1',index1+1)
        return res