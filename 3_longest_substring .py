# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 14:33:20 2018

@author: Evan_He
"""
        
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        # first version
        if len(s)==0:
            return 0
        dic = []
        count = []
        n = len(s)
        for i in range(n):
            if s[i] in dic:
                count.append(len(dic))
                index = dic.index(s[i])
                if index ==len(dic):
                    dic=[]
                else:
                    dic = dic[index+1:]
            dic.append(s[i])
            if i ==n-1:
                count.append(len(dic))
                
        if len(count)==0:
            return n 
        return max(count)
        """
        
        """
        # second version
        if len(s)==0:
            return 0
        dic = []
        count = []
        n = len(s)
        for i in range(n):
            try:
                index = dic.index(s[i])
                count.append(len(dic))
                if index ==len(dic):
                    dic=[]
                else:
                    dic = dic[index+1:]
            except:
                pass
            dic.append(s[i])
            if i ==n-1:
                count.append(len(dic))
                
        if len(count)==0:
            return n 
        return max(count)
        """
        #third version
        if s=="":
            return 0
        i = -1
        result = 0
        dic={}
        for index,value in enumerate(s):
            if value in dic and i<=dic[value]:
                i=dic[value]
            dic[value]=index
            if index - i>result:
                result = index-i
        return result
        
