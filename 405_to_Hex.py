# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 00:05:46 2018

@author: Evan_He
"""

class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num += 2**32
        if num == 0:
            return '0'
        
        alp = ['a','b','c','d','e','f']
        res = ''
        while num != 0:
            ram = num%16
            if ram < 10:
                res = str(ram)+res
            else:
                res = alp[ram-10]+res
            num //= 16
        return res
    
        """hex(num)[2:]#直接求十六进制"""