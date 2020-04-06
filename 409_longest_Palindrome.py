# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:24:35 2018

@author: Evan_He
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        sigle = 0
        s_unique = set(s)
        for si in s_unique:
            count = s.count(si)
            if count%2==0:
                length += count
            else:
                length += count-1
                sigle +=1
        if sigle != 0:
            length += 1
        return length
            
    