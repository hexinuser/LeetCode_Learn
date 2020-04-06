# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:29:26 2018

@author: Evan_He
"""

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        def simplify(M):
            b=[]
            for m in M:
                if m=='#':
                    if b !=[]:
                        b.pop()
                else:
                    b.append(m)
            return b
        return simplify(S)==simplify(T)