# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 12:26:48 2018

@author: Evan_He
"""

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
        def count(in_str):
            dict_count = {}
            for alp in in_str:
                if alp in dict_count:
                    dict_count[alp] += 1
                else:
                    dict_count[alp] = 0
            return dict_count
        return count(s)==count(t)
        """
        if len(s)!=len(t):
            return False
        set_s = set(s)
        for alp in set_s:
            if s.count(alp) != t.count(alp):
                return False
        return True