# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 13:57:20 2018

@author: Evan_He
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        """
        result = []
        for num in range(left,right+1):
            t=set(str(num))
            if '0' in t:
                continue
            test = True
            for k in t:
                if num%(int(k))!=0:
                    test=False
                    
            if test:
                result.append(num)
        return result
            
        """
        result = []
        for i in range(left, right+1):
            j = i
            while j:
                d = j % 10
                if not d: #d=0, j 不是自除数
                    break
                if i % d: #不能整除
                    break
                j = j//10
            if not j: 
                result.append(i)
        return result