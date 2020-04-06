# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 22:59:05 2018

@author: Evan_He
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {'I':1,'V':5,'IV':4,'IX':9,'X':10,'L':50,'C':100,'XL':40,'XC':90,'CD':400,
              'CM':900,'M':1000,'D':500}
        n = len(s)
        k=0
        result = 0
        while k<n-1:
            if s[k:k+2] in ['IV','IX','XL','XC','CM','CD']:
                result += dic[s[k:k+2]]
                k+=2
            else:
                result += dic[s[k]]
                k+=1
        if k!=n:
            result += dic[s[-1]]
        return result
        
        """
        n = len(s)
        k=0
        result = 0
        while k<n:
            if s[k]=='I':
                if k<n-1:
                    if s[k+1]== 'V':
                        result += 4
                        k += 1
                    elif s[k+1]== 'X':
                        result += 9
                        k += 1
                    else:
                        result += 1
                else:
                    result += 1
            elif s[k]=='X':
                if k<n-1:
                    if s[k+1]== 'L':
                        result += 40
                        k += 1
                    elif s[k+1]== 'C':
                        result += 90
                        k += 1
                    else:
                        result += 10
                else:
                    result += 10
            elif s[k]=='C':
                if k<n-1:
                    if s[k+1]== 'D':
                        result += 400
                        k += 1
                    elif s[k+1]== 'M':
                        result += 900
                        k += 1
                    else:
                        result += 100
                else:
                    result += 100
            elif s[k]=='V':
                result += 5
            elif s[k]=='L':
                result += 50
            elif s[k]=='D':
                result += 500
            elif s[k]=='M':
                result += 1000
            k+=1

        return result
        """