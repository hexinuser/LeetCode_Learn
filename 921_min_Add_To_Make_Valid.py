# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:31:33 2019

@author: Evan_He
"""

class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stock = []
        for s in S:
            if stock == []:
                stock.append(s)
            elif s == '(':
                stock.append('(')
            else:
                if stock[-1] == ')':
                    stock.append(')')
                else:
                    stock.pop()
        return len(stock)