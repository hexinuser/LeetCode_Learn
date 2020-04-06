# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:46:21 2018

@author: Evan_He
"""

class Solution:
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        a0 = s[0]
        for i in range(1,int(n/2)+1):
            if s[i]==a0:
                if s[:i]*int(n/i)==s:
                    return True
        return False
            