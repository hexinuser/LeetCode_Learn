# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:11:40 2018

@author: Evan_He
"""

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits=="":
            return []
        dic = {'2':['a','b','c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']
              }
        if len(digits)==1:
            return dic[digits[0]]
        else:
            first = dic[digits[0]]
            secound = self.letterCombinations(digits[1:])
            
            return [a+b for a in first for b in secound]