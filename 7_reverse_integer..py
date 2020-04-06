# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 17:14:09 2018

@author: Evan_He
"""

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
#        if x< 0:
#            x1 = -int(str(x)[1:][::-1])
#            if x1 < -2**31:
#                return 0
#            else:
#                return x1
#        else:
#            x1 = int(str(x)[::-1])
#            if x1 > 2**31-1:
#                return 0
#            else:
#                return x1
        if x<0:
            return -self.reverse(-x)
        t=0
        while True:
            t += x%10
            x =x//10
            if x!=0:
                t *=10
            else:
                break
        if t> 2**31-1:
            t = 0
        return t
    
a = Solution()
print(a.reverse(234))