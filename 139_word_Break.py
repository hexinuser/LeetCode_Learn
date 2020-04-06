# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:37:03 2019

@author: Evan_He
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        res = [-1]
        for i in range(1,len(s)+1):
            for j in res:
                if s[j+1:i] in wordDict:
                    res.append(i-1)
                    break
        return res[-1] == (len(s)-1)