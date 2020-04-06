# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:31:49 2019

@author: Evan_He
"""

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        licensePlate = licensePlate.lower()
        alp_dict = {}
        for lic in licensePlate:
            if lic.isalpha():
                alp_dict[lic] = alp_dict.get(lic,0) + 1
        res,length = None,0
        for word in words:
            sign = True
            for key,value in alp_dict.items():
                if word.count(key) < value:
                    sign = False  
            if sign:  
                if not res:
                    length = len(word)
                    res = word
                else:
                    if len(word)<length:
                        length = len(word)
                        res = word 
        return res
                