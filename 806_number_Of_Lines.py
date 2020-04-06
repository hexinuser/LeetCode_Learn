# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 21:53:49 2019

@author: Evan_He
"""

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        """
        T = "abcdefghijklmnopqrstuvwxyz"
        dict_num = {}
        for i in range(26):
            dict_num[T[i]] = widths[i]
        col,res = 1,0
        for alp in S:
            res += dict_num[alp]
            if res > 100:
                col += 1
                res = dict_num[alp]
        return [col,res]
        
        """ #下标索引明显比字典索引慢,但转化为为ASCII码计算较快
        col,res = 1,0
        for alp in S:
            res += widths[ord(alp)-ord('a')]
            if res > 100:
                col += 1
                res = widths[ord(alp)-ord('a')]
        return [col,res]
        