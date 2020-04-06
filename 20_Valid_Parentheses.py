# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:12:53 2018

@author: Evan_He
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {')':'(','}':'{',']':'['}
        
        left = []
        
        for sign in s:
            if sign in mapping: #直接判断键值是否包含
                if left:
                    if mapping[sign]!= left.pop():
                        return False
                else:
                    return False
            else:
                left.append(sign)
        return not left