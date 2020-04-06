# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 17:07:55 2018

@author: Evan_He
"""

class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')