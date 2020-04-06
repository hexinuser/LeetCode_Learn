# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:48:49 2018

@author: Evan_He
"""

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """ #利用数学公式判断数是不是4的幂，不同写法产生不同结果
        def pow4(num):
            if num <= 0 or int(num)!=num:
                return False
            num = int(num)
            num = bin(num)[2:]
            if num.count('1') == 1:
                if (len(num)-num.index('1')) % 2 == 1:
                    return True
            return False
        n *= 3
        return pow4(n+1) or pow4((n+2)/2)
        """
        import math
        def pow4(num):
            if num <= 0 or int(num)!=num:
                return False
            num = int(num)
            t = math.log(num,4)
            return 4**round(t) == num
        n *= 3
        return pow4(n+1) or pow4((n+2)/2)
        """
        bin_num = bin(n)[2:]
        for i in range(len(bin_num)-1):
            if bin_num[i] == bin_num[i+1]:
                return False
        return True
        """