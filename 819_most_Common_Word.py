# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:19:49 2019

@author: Evan_He
"""
class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        paragraph = paragraph.lower()
        """#验证截取
        sign = "!?',; ."
        i,paras = 0,[]
        for j in range(len(paragraph)):
            if paragraph[j] in sign:
                if j>i:
                    paras.append(paragraph[i:j])
                i = j + 1
        if j > i:
            paras.append(paragraph[i:])
        """
        #替换
        paragraph = paragraph.replace(","," ").replace("."," ").replace("!"," ").replace("?"," ").replace(";"," ").replace("'"," ")
        paras = paragraph.split()
        
        
        print(paras)
        res = {}
        for para in paras:
            res[para] = res.get(para,0)+1
        sort_key = sorted(res.keys(),key =lambda x: res[x],reverse=True)

        for key in sort_key:
            if key not in banned:
                break
        return key
