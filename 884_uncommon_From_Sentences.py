# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:37:02 2018

@author: Evan_He
"""

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        from collections import Counter
        A = A.split() + B.split()
        A_dict = Counter(A)
        res = []
        for key,value in A_dict.items():
            if value == 1:
                res.append(key)
        return res