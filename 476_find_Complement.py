# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:01:25 2018

@author: Evan_He
"""

class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        """
        #原理 参考.num+comp = 2**(len(num))-1
        n = 2 
        while n <= num:
            n <<= 1   #等价于 n * = (2**1) 向左按二进制移位1为移动个数，同样有>>=
        return n-1-num
        """
        """
        bin_num = bin(num)[2:]
        list_comp = ['1' if i=='0' else '0' for i in bin_num]
        return int(''.join(list_comp),2)
        """
        return 2**(len(bin(num))-2)-1-num
        