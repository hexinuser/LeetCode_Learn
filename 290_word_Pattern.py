# -*- coding: utf-8 -*-
"""
Created on Thu May  9 11:48:56 2019

@author: Evan_He
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = str.split()
        res = {}
        m, n = len(pattern),len(s)
        if m!=n:
            return False
        for i in range(m):
            if pattern[i] in res:
                if s[i] != res[pattern[i]]:
                    return False
            else:
                if s[i] in res.values():
                    return False
                res[pattern[i]] = s[i]
        return True