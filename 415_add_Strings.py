# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:10:00 2018

@author: Evan_He
"""

class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        dict_num = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'0':0}
        res = ''
        m,n = len(num1),len(num2)
        if m<n:
            m,n,num1,num2 = n,m,num2,num1
        sign = 0
        for i in range(1,n+1):
            n1,n2 = dict_num[num1[-i]],dict_num[num2[-i]]
            t = n1+n2+sign
            if t>=10:
                res = str(t-10)+res
                sign = 1
            else:
                res = str(t)+res
                sign = 0
        if sign==0:
            return num1[:-i]+res
        i = n+1
        while True:
            if i>m:
                return '1'+res
            else:
                t = dict_num[num1[-i]]+1
                if t==10:
                    res = str(0)+res
                    i += 1
                else:
                    return num1[:-i]+str(t)+res
     
        