# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 13:43:44 2018

@author: Evan_He
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def isnum(s):
            if s[0] == '-' or s[0] ==  '+':
                s = s[1:]
            s = s.split('.')
            if len(s) == 1:
                return s[0].isdigit()
            elif len(s) == 2:
                if s[0] == '':
                    return  s[1].isdigit()
                if s[1] == '':
                    return  s[0].isdigit()
                else:
                    return s[0].isdigit() and s[1].isdigit()
            else:
                return False
            
        s = s.strip()
        if not s:
            return False
        s = s.split('e')
        if len(s) == 1:
            return isnum(s[0])
        elif len(s) == 2:
            if s[0] == '' or s[1] == '':
                    return  False
            else:
                if s[1][0] == '-' or s[1][0] ==  '+':
                    s[1] = s[1][1:]
                return isnum(s[0]) and s[1].isdigit()
        else:
            return False
        """
        try:
            float(s)
            return True
        except:
            return False
        """