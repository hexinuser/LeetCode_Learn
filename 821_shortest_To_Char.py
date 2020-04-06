# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:00:34 2018

@author: Evan_He
"""

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        m= len(S)
        res = [0]*m
        index0 = S.find(C)
        res[:index0] = list(range(index0,0,-1))
        index1 = S.find(C,index0+1)
        while index1 != -1:
            n = index1-index0-1
            if n % 2 == 0 and n>0:
                res[index0+1:index1] = list(range(1,n//2+1))+list(range(n//2,0,-1))
            if n % 2 == 1:
                res[index0+1:index1] = list(range(1,n//2+1))+[n//2+1]+list(range(n//2,0,-1))
            index0,index1 = index1, S.find(C,index1+1)
        
        if index0<m-1:    
            res[index0+1:] = list(range(1,m-index0))
        return res