# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:20:40 2018

@author: Evan_He
"""

class Solution:
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        if n<=3:
            return True
        if n == 4:
            return False
        return not self.canWinNim(n-4)
        """
        if n%4==0:
            return False
        else:
            return True
        
        #B要赢必须要A在n-1,n-2,n-3处都要赢