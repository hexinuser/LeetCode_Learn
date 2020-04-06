# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 16:46:33 2019

@author: Evan_He
"""

class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        def find_xy(str_equ):
            x,cons,i,n = 0,0,1,len(str_equ)
            k = 0
            if str_equ[0] not in ['+','-']:
                str_equ = '+'+str_equ
                n += 1
            elif str_equ[0] == 'x':
                x += 1
                i = 2
                k = 1
            str_equ += '+'
            while i <= n:
                if str_equ[i] in ['+','-']:
                    if str_equ[i-1] != 'x':
                        cons += int(str_equ[k:i])
                    else:
                        if k == i-2:
                            x += int(str_equ[k]+'1')
                        else:
                            x += int(str_equ[k:i-1])
                    k = i
                i += 1
            return x,cons
        [left,right] = equation.split('=')
        x1,cons1 = find_xy(left)
        x2,cons2 = find_xy(right)
        if x1 == x2:
            if cons1 == cons2:
                return "Infinite solutions"
            else:
                return 'No solution'
        else:
            return 'x=%d' %((cons2-cons1)//(x1-x2))