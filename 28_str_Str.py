# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:46:33 2018

@author: Evan_He
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1