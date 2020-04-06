# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:31:08 2018

@author: Evan_He
"""

class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        
        
        if rec1[1]>=rec2[3] or rec1[3]<= rec2[1]:
            return False
        if rec1[2]<=rec2[0] or rec1[0]>=rec2[2]:
            return False
        return True