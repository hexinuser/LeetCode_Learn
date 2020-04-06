# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:12:21 2018

@author: Evan_He
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str=s.split(' ')
        for i in range(len(str)):
            str[i]=str[i][::-1]
        return ' '.join(str)
        