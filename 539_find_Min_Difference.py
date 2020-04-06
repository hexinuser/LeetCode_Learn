# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 16:31:23 2018

@author: Evan_He
"""

class Solution:
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        time_min = [int(time[:2])*60+int(time[-2:]) for time in timePoints]
        n = len(time_min)
        time_min.sort()
        time_sub =[time_min[i]-time_min[i-1] for i in range(1,n)]
        time_sub.append(time_min[0]-time_min[-1]+1440)
        return min(time_sub)