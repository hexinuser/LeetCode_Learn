# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:59:05 2019

@author: Evan_He
"""

class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(n**0.5)
    
    #每一个灯泡若翻转奇数次就是开启，偶数次是关闭
    #而翻转次数就是他的所有因子数，而对非完全平方数，因子是成对的
    #故必为偶数次，只需计算n以内的完全平方数的个数即可