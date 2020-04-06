# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 01:07:44 2018

@author: Evan_He
"""

class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        if n==0:
            return False
        else:
            return n&(n-1)==0
        # 运算符&：a&b 表示参与运算的两个值a，b,如果两个相应位都为1,则该位的结果为1,否则为0
        # 如果n是2的幂则 n的二进制位 1000...0, n-1为 0111...1即a&b==0
        """
        
        if n==0:
            return False
        if n==1:
            return True
        else:
            if n%2!=0:
                return False
            else:
                return self.isPowerOfTwo(n//2)
        
        """
        import math
        if n<0:
            return False
        if n==0:
            return False
        t = math.log2(n)
        if t==int(t):
            return True
        return False
      """
