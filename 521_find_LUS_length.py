# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 14:11:13 2019

@author: Evan_He
"""

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        #智障题目
        if a == b:
            return -1
        return max(len(a),len(b))