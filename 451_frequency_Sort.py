# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:56:39 2018

@author: Evan_He
"""

class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        #利用字典
        count_dic = {}
        for i in s:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1
        
        t = sorted(count_dic.items(),key = lambda x:x[1],reverse = True)
        #t = sorted(zip(count_dic.values(),count_dic.keys()),reverse = True)
        res = ''
        for value,n in t:
            res += n*value
        return res
        """
        #利用集合
        set_s = set(s)
        res = []
        for i in set_s:
            res.append((s.count(i),i))
        res = sorted(res,key=lambda x:x[0],reverse=True)
        ans = ''
        for i in res:
            ans += i[0]*i[1]
        return ans
        """