# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 20:08:29 2018

@author: Evan_He
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for op in ops:
            try:  #op.isdigit()不能判断负数
                res.append(int(op))
            except:
                if op == 'C':
                    res.pop()
                elif op == 'D':
                    res.append(res[-1]*2)
                elif op == '+':
                    res.append(res[-1]+res[-2])
        return sum(res)