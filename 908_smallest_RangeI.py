# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 20:41:44 2018

@author: Evan_He
"""

class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        return max(max(A)-min(A)-2*K,0)