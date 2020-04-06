# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:16:02 2018

@author: Evan_He
"""
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #return str.lower()
        result = ''
        for i in range(len(str)):
            if str[i]>='A' and str[i]<='Z':
                result+= chr(ord(str[i])+32)
            else:
                result +=str[i]
                
        return result
        