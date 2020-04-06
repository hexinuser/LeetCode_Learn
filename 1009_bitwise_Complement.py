# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:40:25 2019

@author: Evan_He
"""

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 2**(len(bin(N))-2)-1-N