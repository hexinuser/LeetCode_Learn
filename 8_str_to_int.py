# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:38:30 2018

@author: Evan_He
"""

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        import re
        str =str.strip()
        if str== '':
            return 0
        if str[0]=='-':
            try:
                t = -int(re.match('(\d+)',str[1:]).group())
                if t>2**31-1:
                    return 2**31-1
                elif t<-2**31:
                    return -2**31
                else:
                    return t
            except:
                return 0
        elif str[0]=='+':
            try:
                t = int(re.match('(\d+)',str[1:]).group())
                if t>2**31-1:
                    return 2**31-1
                elif t<-2**31:
                    return -2**31
                else:
                    return t
            except:
                return 0
        else:
            try:
                t = int(re.match('(\d+)',str).group())
                if t>2**31-1:
                    return 2**31-1
                elif t<-2**31:
                    return -2**31
                else:
                    return t
            except:
                return 0