# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:28:18 2019

@author: Evan_He
"""

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m,n = len(name),len(typed)
        if m > n:
            return False
        if name[0]!=typed[0]:
            return False
        i,j = 1,1
        while i < m and j<n:
            if name[i] == typed[j]:
                j += 1
                i += 1
            else:
                if typed[j] != name[i-1]:
                    return False
                while j < n:
                    if typed[j] == name[i-1]:
                        j += 1
                    else:
                        break
        return i == m