# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:08:19 2018

@author: Evan_He
"""

class Solution:
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=a.split('+')
        b=b.split('+')
        a_real = int(a[0])
        a_imag = int(a[1][:-1])
        b_real = int(b[0])
        b_imag = int(b[1][:-1])
        
        c_real = a_real*b_real-a_imag*b_imag
        c_imag = a_real*b_imag+a_imag*b_real
        
        return str(c_real)+'+'+str(c_imag)+'i'