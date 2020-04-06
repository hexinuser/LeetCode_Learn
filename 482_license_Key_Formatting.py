# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 21:37:37 2018

@author: Evan_He
"""

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = ''.join(S.upper().split('-'))
        n = len(S)
        k = n%K
        res = []
        if k !=0:
            res.append(S[:k])
            res += [S[k+K*i:k+K*i+K] for i in range(n//K)]
        else:
            res += [S[K*i:K*i+K] for i in range(n//K)]
        return '-'.join(res)