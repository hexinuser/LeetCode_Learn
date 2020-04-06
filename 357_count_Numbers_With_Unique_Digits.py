# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 10:43:59 2019

@author: Evan_He
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        #每个数字不同最多十位数, 对于n,若第一个元素为0,则其个数为 res(n-1)
        #若第一位不为0, 则第一位有九种选择, 剩下的在剩余的九个中选n-2个即可
        if n == 0:
            return 1
        if n == 1:
            return 10
        k = 2
        res1 = 10
        while k<=n:
            mid = 9
            for i in range(1,k):
                mid *= 9-i+1
            res1 += mid
            k += 1
        return int(res1)