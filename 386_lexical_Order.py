# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:41:47 2018

@author: Evan_He
"""

class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        
        res = list(map(str,range(1,n+1)))
        res.sort()
        return list(map(int,res))
        #return sorted([i for i in range(1,n+1)],key = str) #简化
        """表示到统一两集，排序
        import math
        top = int(math.log10(n)) + 1
        def mycmp(a):
            while a < top:
                a *= 10
            return a
        return sorted(range(1, n + 1), key=mycmp)
        """