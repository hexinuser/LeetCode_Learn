# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:17:01 2018

@author: Evan_He
"""

class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        """
        both_res = set(list1).intersection(set(list2))
        res = []
        min_index = 1e4
        for both in both_res:
            t = list1.index(both) + list2.index(both)
            if t == min_index:
                res.append(both)
            elif t < min_index:
                res = [both]
                min_index = t
        return res
        """
        dict_res = {}
        for i,value in enumerate(list2):
            dict_res[value] = i
        min_index = 1e4
        res = []
        for i in range(len(list1)):
            if list1[i] in dict_res:
                t = i + dict_res[list1[i]]
                if t == min_index:
                    res.append(list1[i])
                elif t < min_index:
                    res = [list1[i]]
                    min_index = t
        return res
        