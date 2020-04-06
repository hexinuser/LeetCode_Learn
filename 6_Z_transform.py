# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:36:08 2018

@author: Evan_He
"""

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        """
        #frist version
        if len(s)==0: return ""
        if numRows==1: return s
        n,result,k = len(s),'',numRows*2-2
        for i in range(numRows):
            if i==0 or i==numRows-1:
                a = [s[j] for j in range(i,n,k)]
            else:
                a=[]
                for j in range(i,n,k):
                    if j+k-i*2<n:
                        a.extend([s[j]+s[j+k-i*2]])
                    else:
                        a.append(s[j])
            result+=''.join(a)
        return result
        """
        if len(s)==0: return ""
        if numRows == 1: return s
        result_list = [''] * numRows
        index, up_down = 0, 1
        for x in s:
            result_list[index] += x
            if index == 0:
                up_down = 1
            elif index == numRows - 1:
                    up_down = -1
            index += up_down
        return ''.join(result_list)        