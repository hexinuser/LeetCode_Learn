# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:51:33 2019

@author: Evan_He
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        count_num = Counter(p)
        m = len(p)
        count_s,k = {},0
        res = []
        for i in range(len(s)):
            if s[i] not in count_num:
                count_s = {}
                k = 0
                continue
            else:
                count_s[s[i]] = count_s.get(s[i],0)+1
                if count_s[s[i]] > count_num[s[i]]:
                    if s[i-k] != s[i]:
                        while s[i-k] != s[i]:
                            count_s[s[i-k]] -= 1
                            k -= 1
                    count_s[s[i]] -= 1
                    k -= 1
                k += 1
                if k == m:
                    res.append(i-k+1)
                    count_s[s[i-k+1]] -= 1
                    k -= 1
        return res