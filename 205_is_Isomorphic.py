# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:13:23 2019

@author: Evan_He
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        save_dict = {}
        for i in range(len(s)):
            if s[i] in save_dict:
                if t[i] != save_dict[s[i]]:
                    return False
            else:
                if t[i] in save_dict.values():
                    return False
                save_dict[s[i]] = t[i]
        return True