# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:02:24 2019

@author: Evan_He
"""

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        S = list(S)
        i,j = 0,len(S)-1
        while i < j:
            if not S[i].isalpha():
                i += 1
                continue
            if not S[j].isalpha():
                j -= 1
                continue
            S[i],S[j] = S[j],S[i]
            i += 1
            j -= 1
        return ''.join(S)

        