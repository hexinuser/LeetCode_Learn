# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 23:55:45 2019

@author: Evan_He
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        return ' '.join(s[::-1])