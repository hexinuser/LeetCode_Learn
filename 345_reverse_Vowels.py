# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 21:28:57 2019

@author: Evan_He
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        i,j = 0,len(s)-1
        s = [i for i in s]
        vowel = set(['a','e','i','o','u','A','E','I','O','U'])
        while i < j:
            while s[i] not in vowel:
                i += 1
                if i >= j:
                    break
            while s[j] not in vowel:
                j -= 1
                if j <= i:
                    break
            if i < j:
                s[i],s[j] = s[j],s[i]
            else:
                break
            i += 1
            j -= 1
        return ''.join(s)