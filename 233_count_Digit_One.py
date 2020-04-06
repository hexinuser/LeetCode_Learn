# -*- coding: utf-8 -*-
"""
Created on Thu May  2 22:28:45 2019

@author: Evan_He
"""

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n < 10:
            return 1

        else:
            n = str(n)
            a,b = int(n[0]),int(n[1:])
            if a == 1:
                return 1+b+self.countDigitOne(b)+self.countDigitOne(10**(len(n)-1)-1)
            else:
                return 10**(len(n)-1)+self.countDigitOne(b)+a*self.countDigitOne(10**(len(n)-1)-1)