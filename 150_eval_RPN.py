# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 19:50:09 2018

@author: Evan_He
"""

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result = []
        sign = ['+','-','*','/']
        for token in tokens:
            if token in sign:
                if token == "+":
                    result[-2] += result[-1]
                if token == "-":
                    result[-2] -= result[-1]    
                if token == "*":
                    result[-2] *= result[-1]
                if token == "/":
                    result[-2] = int(result[-2]/result[-1])
                result.pop()
            else:
                result.append(int(token))
        return result[0]
            