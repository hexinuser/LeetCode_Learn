# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:34:13 2019

@author: Evan_He
"""

class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = [ i for i in str(num)]
        num_sort = sorted(num_str,reverse = True)
        for i in range(len(num_str)):
            if num_sort[i] != num_str[i]:
                j = len(num_str) - num_str[::-1].index(num_sort[i]) - 1
                num_str[i],num_str[j] = num_str[j],num_str[i]
                break
        return int(''.join(num_str))