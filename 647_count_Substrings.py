# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 00:37:06 2018

@author: Evan_He
"""

class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """# 和第五题的Manacher算法可直接计算每个中心点的回文串个数，累加即可"""
        T = '#'+'#'.join(s)+'#'
        n = len(T)
        P = [1 for _ in range(n)]
        mid = 0
        bound = 0
        i = 0
        while i <n:
            if bound>i:                     
                P[i] = min(bound-i,P[2*mid-i])
            while i-P[i]>=0 and i+P[i]<n:
                if T[i-P[i]] == T[i+P[i]]:
                    P[i] +=1
                else:
                    break
            if i+P[i]>bound:
                mid = i
                bound = i+P[i]
            i += 1
        count = 0
        for i in range(n):
            count += P[i]//2
        return count   