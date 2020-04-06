# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 23:17:07 2018

@author: Evan_He
"""

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        """#正向，从最大到最小
        import math
        if num==0:
            return '0'
        if num<0:
            return '-'+self.convertToBase7(-num)
        res = ''
        n = int(math.log(num,7))
        while n>=0:
            t = num//(7**n)
            num %= (7**n) 
            res += str(t)
            n -= 1
        return res
        """
        #反向从最小到最大
        if num==0:
            return '0'
        if num<0:
            return '-'+self.convertToBase7(-num)
        res = ''
        while num>0:
            t = num%7
            res = str(t)+res
            num //= 7
        return res
            
        