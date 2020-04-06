# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:11:15 2018

@author: Evan_He
"""

class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #可和算法389相同
        dict_s = {}
        for alp in magazine:
            dict_s.setdefault(alp,0)
            dict_s[alp] += 1
        for alp in ransomNote:
            if alp not in dict_s:
                return False
            else:
                dict_s[alp] -= 1
                if dict_s[alp] < 0:
                    return False
        return True
        """
        for alp in ransomNote:
            if alp in magazine:
                magazine = magazine.replace(alp,"",1)
            else:
                return False
        return True
        """