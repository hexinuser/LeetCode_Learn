# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 14:14:01 2019

@author: Evan_He
"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        i,n = 0,len(seats)
        res = []
        while True:
            try:
                j = seats[i:].index(1)
                if i == 0 and j != 0:
                    res.append(j)
                else:
                    res.append((j+1)//2)
                i += j+1
            except:
                break
        res.append(n-i)
        return max(res)