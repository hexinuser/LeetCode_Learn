# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 00:47:34 2018

@author: Evan_He
"""

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==1:
            return ["()"]
        A =[]
        tn = self.generateParenthesis(n-1)
        for t in tn:
            A += ['()'+t]+['('+t+')']  #计算第n个括号中间为空或者为n-1的样本
        for i in range(1,n-1):
            ti0 = self.generateParenthesis(i)    #'()'中间i个，后边n-i个（n-i小于n-1）
            ti1 = self.generateParenthesis(n-i-1)
            for t0 in ti0:
                for t1 in ti1:
                    A += ['('+t0+')'+t1]
        return A