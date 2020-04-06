# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 17:52:39 2019

@author: Evan_He
"""

class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count_alpha = collections.Counter(s)  #对字母记数
        res,res_set = [], set()   #res_set为结果的集合形式，set判断包含关系相对列表判断较快
        for alpha in s:
            if alpha in res_set:
                count_alpha[alpha] -= 1 #对已经包含在结果的字母忽视，减少计数
            else:
                #当字母不在结果中，按栈依次比较结果，判断是否去除最后一位元素
                while res and alpha < res[-1] and count_alpha[res[-1]] > 1:
                    #当结果不空，且当前字母比结果的最后一个字母小（其在当前alpha后方的个数不为0）时，删除
                    last = res.pop()
                    res_set.remove(last)
                    count_alpha[last] -= 1
                #更新alpha到结果res中
                res.append(alpha)
                res_set.add(alpha)
        return ''.join(res) #将结果列表转化为字符串