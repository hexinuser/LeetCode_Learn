# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:44:05 2018

@author: Evan_He
"""

class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        t = s.strip().split()
        return len(t)