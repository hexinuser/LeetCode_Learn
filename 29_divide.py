# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:14:02 2019

@author: Evan_He
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        #位运算 dividend - 2^k *divisor // divisor
        i, a, b = 0, abs(dividend), abs(divisor)
        if a == 0 or a < b:
            return 0
        while b <= a:
            b = b << 1
            i = i + 1
        else:
            res = (1 << (i - 1)) + self.divide(a - (b >> 1), abs(divisor))
            if (dividend ^ divisor) < 0:
                res = -res
        return min(res, (1 << 31) - 1)
    '''
    python位运算符：python的位运算符是把数字看作二进制来进行计算的。
    按位与（&）：如果两个二进位都为1，则该位结果为1，否则为0
    按位或（|）：只要一个为1，则为1，否则为0
    按位异或（^）：两个二进位相异为为1（即两个二进位要相反），否则为0
    取反（~）：对数据的每个二进制位取反，即把1变0，把0变1
    左移动：运算数的各二进位全部向左移若干位
    右移动：运算数的各二进位全部向右移若干位


    a = 60  #60的二进制为 0011 1100
    b = 13  #13的二进制为 00001101
    c = 0
    #按位与的运算方法如下：（按位或、按位异或也是一样）
    #即  a 0011 1100
    #    b 0000 1101
    #得出 c 0000 1100
    c = a & b
    print('a与b的按位与运算结果为：',c)  #结果为 0000 1100
    c = a | b
    print('a与b的按位或运算结果为：',c)   #结果为 0011 1101
    c = a ^ b
    print('a与b的按位异或运算结果为：',c)   #结果为 0011 0001
    c = ~a
    print('a按位取反运算为：',c)    #结果为  1100 0011
    c = a << 3
    print('a左移动3运算为：',c)    #结果为  1111 0000 0
    c = a >> 3
    print('a右移动3运算为：',c)    #结果为  0000 0111
    '''