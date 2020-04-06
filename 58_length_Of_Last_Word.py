# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 23:54:26 2018

@author: Evan_He
"""

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s)==0:
            return 0
        return len(s.split()[-1])