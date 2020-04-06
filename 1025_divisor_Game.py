# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:23:58 2019

@author: Evan_He
"""

class Solution:
    def divisorGame(self, N: int) -> bool:
        """
        归纳法可证明：
        如果对N是为False,那么当N+1时只需要取x=1, 那么N+1结果必定为True
        显然可以判断 1,2分别位False,True, 不妨假设对任意小于N的奇数为False,偶数为True
        那么对于N:
            如果N为偶数，那么N-1为奇数False,得N为True
            如果N为奇数，那么N的因数x必定为奇数, 则N-x为偶数必定为True, 得到N为False
        """
        return N%2==0