# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:58:36 2018

@author: Evan_He
"""

class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ifnot=[]
        while True:
            if n in ifnot:
                return False
            ifnot.append(n)
            num=str(n)
            n=sum([int(i)**2 for i in num])
            if n==1:
                return True
