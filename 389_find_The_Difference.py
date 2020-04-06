# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 23:35:42 2018

@author: Evan_He
"""

class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict_s = {}
        for alp in s:
            dict_s.setdefault(alp,0)
            dict_s[alp] += 1
        for alp in t:
            if alp not in dict_s:
                return alp
            else:
                dict_s[alp] -= 1
                if dict_s[alp] < 0:
                    return alp