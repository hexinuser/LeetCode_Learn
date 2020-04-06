# -*- coding: utf-8 -*-
"""
Created on Sun May  5 19:22:41 2019

@author: Evan_He
"""

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        k = 0
        res = ''
        res_l = [S[0]]
        i = 1 
        while i < len(S):
            if S[i] == '(':
                res_l.append("(")
            else:
                if res_l[-1] == '(':
                    res_l.pop()
                    if not res_l:
                        res += S[k+1:i]
                        k = i+1
                else:
                    res_l.append(")")
            i += 1
        return res
            