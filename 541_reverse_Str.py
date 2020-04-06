# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 22:59:30 2018

@author: Evan_He
"""

class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        """
        res = ''
        n = len(s)
        cons = n//(2*k)
        remain = n%(2*k)
        for i in range(cons):
            res += s[i*2*k:i*2*k+k][::-1]
            res += s[i*2*k+k:(i+1)*2*k]
        if remain<k:
            res += s[cons*2*k:][::-1]
        else:
            res += s[cons*2*k:cons*2*k+k][::-1]
            res += s[cons*2*k+k:]
        return res
        """
        # 字符串末端超出下表读取返回空字符串“”不影响结果
        i = 0
        res = ''
        n = len(s)
        while i < n:
            res += s[i:i+k][::-1]
            res += s[i+k:i+2*k]
            i += 2*k
        return res
    
