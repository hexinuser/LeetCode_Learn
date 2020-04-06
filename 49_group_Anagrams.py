# -*- coding: utf-8 -*-
"""
Created on Mon May  6 16:06:49 2019

@author: Evan_He
"""

class Solution:
    #可以用质数表示26个字母，把字符串的各个字母相乘，这样可保证字母异位词的乘积必定是相等的
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t in res:
                res[t].append(s)
            else:
                res[t] = [s]
        return list(res.values())