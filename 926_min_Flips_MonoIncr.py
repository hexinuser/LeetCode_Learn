# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 19:03:30 2018

@author: Evan_He
"""
class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        n_0 = S.count('0')
        n = len(S)
        res = n-n_0
        count_before = 0 
        i = 0
        while i < n:
            if S[i] != '0':
                break
            i += 1
        n_0 -= i
        while i < n:
            if S[i] == '1':
                res = min(res,n_0+count_before)
                count_before += 1
            else:
                n_0 -= 1
                res = min(res,n_0+count_before)
                if n_0 == 0:
                    break
            i += 1
        return res
        """ 
        #简化版
        n_0 = S.count('0')
        n = len(S)
        res = n-n_0
        count = 0
        for i in range(n):
            if S[i] == '0':
                n_0 -= 1
            else:
                res = min(res,n_0+count)
                count += 1
        return res
 