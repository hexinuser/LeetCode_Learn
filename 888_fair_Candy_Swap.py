# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 10:16:04 2018

@author: Evan_He
"""

class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        """ #可返回所有
        t = int((sum(B)-sum(A))/2)
        B = [num-t for num in B]
        uni = list(set(A).intersection(set(B)))
        return [uni[0],uni[0]+t]
        """
        t = (sum(B)-sum(A))//2
        B = set(B)
        for num in A:
            if num+t in B:
                return [num,num+t]