# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 09:55:57 2019

@author: Evan_He
"""

class Solution:
    def clumsy(self, N: int) -> int:
        res = 0
        if N <= 2:
            return N
        elif N == 3:
            return 6
        else:
            res += N*(N-1)//(N-2)+ N-3
            N -= 4
        while N >= 4:
            res -= N*(N-1)//(N-2)-(N-3)
            N -= 4
        if N == 3:
            res -= 6
        elif N == 2:
            res -= 2
        elif N == 1:
            res -= 1
        return res
        """#简写版
        num_l = [1,2,6]
        res = 0
        if N <= 3:
            return num_l[N-1]
        else:
            res += N*(N-1)//(N-2)+ N-3
            N -= 4
        while N >= 4:
            res -= N*(N-1)//(N-2)-(N-3)
            N -= 4
        if N != 0:
            res -= num_l[N-1]
        return res
        """