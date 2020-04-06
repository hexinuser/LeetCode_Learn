# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 13:27:46 2018

@author: Evan_He
"""

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """
        import math
        if num <= 0:
            return False
        t = math.log(num,4)
        return 4**round(t) == num
        """#利用二进制数来判定，同样可以判断8的幂
        if num <= 0:
            return False
        num = bin(num)[2:]
        if num.count('1') == 1:
            if (len(num)-num.index('1')) % 2 == 1:
                return True
        return False
    #
