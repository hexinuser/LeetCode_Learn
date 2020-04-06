# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 15:46:12 2019

@author: Evan_He
"""

class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        def judge_prime(num):
            if num <= 1:
                return 0
            elif num <= 3:
                return 1
            t = int(num**0.5)+1
            for i in range(2,t):
                if num%i == 0:
                    return 0
            return 1
            
        res = 0
        while L <= R:
            t = bin(L)[2:].count('1')
            res += judge_prime(t)
            L += 1
        return res
    
    """#10^6以内的数表示成二进制最多20位，即1的个数最多二十位，只需考虑二十以内的素数
        res = 0
        for i in range(L, R + 1):
            if bin(i).count('1') in [2,3,5,7,11,13,17,19]:
                res += 1
        return res
    """