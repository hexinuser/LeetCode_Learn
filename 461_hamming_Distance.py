# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:51:45 2018

@author: Evan_He
"""

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        c = bin(x^y)[2:]
        for i in c:
            if i=='1':
                count+=1
        return count
        
        
        """
        x="{0:b}".format(x)
        y=bin(y)[2:]#bin(y)[.replace('0b','')]
        
        m=len(x)
        n=len(y)
        count=0
        add_xy=str(int(x)+int(y))
        for i in range(max(m,n)):
            if add_xy[i]=='1':
                    count+=1
        return count
        """
        '''
        x="{0:b}".format(x)
        y=bin(y)[2:]#bin(y)[.replace('0b','')]
        
        m=len(x)
        n=len(y)
        count=0
        add_xy=str(int(x)+int(y))
        if m>n:
            for i in range(n):
                if add_xy[m-n+i]=='1':
                    count+=1
            for i in range(n,m):
                if x[i-n]=='1':
                    count+=1
        else:
            for i in range(m):
                if add_xy[n-m+i]=='1':
                    count+=1
            if m!=n:
                for i in range(m,n):
                    if y[i-m]=='1':
                        count+=1
        return count
        '''