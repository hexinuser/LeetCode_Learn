# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:05:51 2019

@author: Evan_He
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        
        intervals = sorted(intervals,key=lambda x: x.start)
        res = []
        i,j = 1,0
        while i < len(intervals):
            if intervals[i].start > intervals[j].end:
                res.append(intervals[j])
                j = i
                i += 1
            else:
                intervals[j].end = max(intervals[i].end,intervals[j].end)
                intervals[j].start = min(intervals[i].start,intervals[j].start)
                i += 1
        res.append(intervals[j])
            
        return res