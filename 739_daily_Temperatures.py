# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 23:20:52 2019

@author: Evan_He
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stock = []
        res = [0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            if stock == [] or temp <= stock[-1][0]:
                stock.append((temp,i))
            else:
                while temp > stock[-1][0]:
                    t = stock.pop()
                    res[t[1]] = i-t[1]
                    if stock == []:
                        break
                stock.append((temp,i))
        return res