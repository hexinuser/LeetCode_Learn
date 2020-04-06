# -*- coding: utf-8 -*-
"""
Created on Thu Dec 13 23:48:29 2018

@author: Evan_He
"""

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        """
        m, n = len(A), len(A[0])
        count = 0
        for i in range(n):
            for j in range(m-1):
                if A[j][i] > A[j+1][i]:
                    count += 1
                    break
        return count
        """
        
        """
        count = 0
        n = len(A[0])
        for col in zip(*A):  #利用zip(*)转置数组
            # 也可考虑
            for i in range(0, n- 1):
                if col[i] > col[i+1]:
                    count += 1
                    break
        return count
        """
        
        count = 0
        for col in zip(*A):#利用zip(*)转置数组
            if list(col) != sorted(col): 
            #判断每一列是否已排序好(元组利用sorted会转化为列表),对大多数已排序好的列表进行排序较快
            #但若列表很大，且完全随机，则排序本身的复杂的就会过高，得不偿失
                count += 1
        return count
    
