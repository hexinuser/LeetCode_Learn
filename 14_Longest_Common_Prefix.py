# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 23:08:23 2018

@author: Evan_He
"""

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n==0 or strs[0]=="":
            return ""
        if n==1:
            return strs[0]
        m = len(strs[0])
        count = 0
            
        for i in range(m):
            for j in range(n-1):
                try:
                    if strs[j][i]!=strs[j+1][i]:
                        if count==0:
                            return ""
                        else:
                            return strs[0][:count]
                except:
                    return strs[0][:count]
            count +=1
        return strs[0][:count]