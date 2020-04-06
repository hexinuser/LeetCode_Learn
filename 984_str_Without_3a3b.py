# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 14:34:13 2019

@author: Evan_He
"""

class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A > B:
            if A > 2*B:
                return 'aab'*B+'a'*(A-2*B)
            else:
                return 'aab'*(A-B)+'ab'*(2*B-A)
        elif A < B:
            if B > 2*A:
                return 'bba'*A+'b'*(B-2*A)
            else:
                return 'bba'*(B-A)+'ba'*(2*A-B)
        else:
            return 'ab'*A