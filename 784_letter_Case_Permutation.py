# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 20:44:26 2018

@author: Evan_He
"""

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        #计算字符的acsii码判断
        if S == '':
            return ['']
        num = ord(S[0])
        if num < 65:
            return [S[0]+ i for i in self.letterCasePermutation(S[1:])]
        elif num < 97:
            return [S[0]+ i for i in self.letterCasePermutation(S[1:])]+\
                [chr(num+32)+ i for i in self.letterCasePermutation(S[1:])]
        else:
            return [S[0]+ i for i in self.letterCasePermutation(S[1:])]+\
            [chr(num-32)+ i for i in self.letterCasePermutation(S[1:])]
        """
        res = ['']
        for s in S:
            if s.isalpha(): #判断字符是否是字母
                res = [i + j for i in res for j in [s.upper(), s.lower()]]
            else:
                res = [i + s for i in res]
        return res
        """