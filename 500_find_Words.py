# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:05:55 2018

@author: Evan_He
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        X1='qwertyuiop'
        X2='asdfghjkl'
        X3='zxcvbnm'
        result=[]
        for i in range(len(words)):
            X=words[i].lower()
            if X[0] in X1:
                if set(X).issubset(X1):
                    result.append(words[i])
            elif X[0] in X2:
                if set(X).issubset(X2):
                    result.append(words[i])
            else:
                if set(X).issubset(X3):
                    result.append(words[i])
        return result