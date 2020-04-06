# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 23:49:44 2019

@author: Evan_He
"""

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        #两种不同写法，前缀和取模，若对应值相同则表示在对应端和值整除
        #对单独值为0表示該值也能作为单独序列满足条件，故对res取初值为[0]
        res = [0]
        for i in range(len(A)):
            res.append((res[-1]+A[i])%K)
        count = collections.Counter(res)
        return int(sum(k*(k-1)/2 for k in count.values()))
        """#两种不同的计数方式
        save = {0:1}
        t = 0
        for i in range(len(A)):
            t = (t+A[i])%K
            save[t] = save.get(t,0) + 1
        return int(sum(k*(k-1)/2 for k in save.values()))
        """
        """
        #n^2的复杂度
        res = 0
        saves = []
        save_z = 0
        for a in A:
            t = a%K
            if t != 0:
                save_z = 0
                for i in range(len(saves)):
                    k = (saves[i]+t)%K
                    if k == 0:
                        res += 1
                        save_z += 1
                    saves[i] = k
            else:
                save_z += 1
                res += save_z
            saves.append(t)
        return res
        """
            
                