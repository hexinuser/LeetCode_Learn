# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:09:45 2018

@author: Evan_He
"""

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        """
        #利用循环来计算1+...+n
        if target < 0:
            target = -target
        k = 0
        res = 0
        while True:
            res += k
            if res >= target:
                if res == target:
                    return k
                if (res-target)%2==0:
                    return k
                else:
                    if (k+1) % 2 == 0: 
                        return k+2
                    else:
                        return k+1
            k += 1
            """
        # 计算 n
        if target < 0:
            target = -target
        n = int((2*target+0.25)**(0.5)-0.5)
        res = int(n*(n+1)/2)
        if res < target:
            n += 1
            res += n
        if (res-target)%2==0:
            return n
        else:
            if (n+1) % 2 == 0: 
                return n+2
            else:
                return n+1
