# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:59:25 2018

@author: Evan_He
"""

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and 'LLL' not in s