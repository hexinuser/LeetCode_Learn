# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 20:43:03 2018

@author: Evan_He
"""

class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        """
        return pow(a, int(''.join(map(str, b))), 1337)
        """
        ## a^(10*b)的余数为a^b的余数的十次方的余数
        res = 1
        for num in b:
            res = res**10 * a**num % 1337
        return res
        """
        a = a%1337
        b = int(''.join(map(str,b)))
        return self.bisection(a,b)
        
    def bisection(self,a,b):
        if b==0:
            return 0
        if b==1:
            return a
        if b%2==0:
            return (self.bisection(a,b//2)**2)%1337
        else:
            return (self.bisection(a,b//2)**2*a)%1337
        """
        
        
        