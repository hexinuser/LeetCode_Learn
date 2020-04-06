# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:51:03 2018

@author: Evan_He
"""

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        result=0
        for i in range(n):
            t=ord(s[i])-64   #利用ord返回大写字母的Unicode code #A:64 ,'a'：97
            result +=26**(n-i-1)*t
        return result