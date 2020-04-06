# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:10:52 2018

@author: Evan_He
"""

class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = set()
        for a in A:
            if a in res:
                return a
            else:
                res.add(a)
        """#count
        return (sum(A)-sum(set(A)))//(len(A)//2-1)
        """