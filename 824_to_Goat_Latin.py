# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 14:37:49 2019

@author: Evan_He
"""

class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        vol = ['a','A','e','E','i','I','o','O','u','U']
        S = S.split()
        for i, w in enumerate(S):
            if w[0] in vol:
                S[i] = w+'ma'+'a'*(i+1)
            else:
                S[i] = w[1:]+w[0]+'ma'+'a'*(i+1)
        return ' '.join(S)