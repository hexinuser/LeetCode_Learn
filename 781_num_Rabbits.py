# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 23:46:52 2019

@author: Evan_He
"""

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        from collections import Counter
        import math
        count_num = Counter(answers)
        res = 0
        for key,val in count_num.items():
            if key == 0:
                res += val
            else:
                if val<= key+1:
                    res += key+1
                else:
                    res += math.ceil(val/(key+1))*(key+1)