# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 14:12:29 2018

@author: Evan_He
"""

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        """
        count = 0
        for i in range(1,N+1):
            if set(str(i)).issubset(set('0182569')):
                if set(str(i)).intersection('2569'):
                    count+=1
        return count
        """
        count = 0
        for i in range(1,N+1):
            i = set(str(i))
            if '3' not in i and '4' not in i and '7' not in i:
                if '0' in i or '1' in i or '8' in i:
                    if '2'  in i or '5'  in i or '6'  in i or '9'  in i:
                        count+=1
                else:
                    count+=1
        return count