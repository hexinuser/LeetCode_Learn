# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:00:34 2018

@author: Evan_He
"""

class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        res = []
        n = len(S)
        i,j = 0,n
        for s in S:
            if s == 'I':
                res.append(i)
                i += 1 
            else:
                res.append(j)
                j -= 1
        res.append(j)
        return res