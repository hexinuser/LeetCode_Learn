# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:20:56 2018

@author: Evan_He
"""

class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        m,n = len(g),len(s)
        i,j,res = 0,0,0
        while i<m and j<n:
            if g[i] <= s[j]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1
        return res