# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:47:26 2018

@author: Evan_He
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        s = s.lower()
        import re
        re_comp = re.compile('[a-z0-9]')
        re_list = re_comp.findall(s)
        return re_list == re_list[::-1]
        """
        s = s.lower()
        dic = 'abcdefghijklmnopqrstuvwxyz1234567890'
        s = [i for i in s if i in dic ]
        return s == s[::-1]