# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 20:38:00 2018

@author: Evan_He
"""

class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(M), len(M[0])
        res = [[0] * n for _ in M]

        for i in range(m):
            for j in range(n):
                count = 0
                for n_i in (i-1, i, i+1):
                    for n_j in (j-1, j, j+1):
                        if 0 <= n_i < m and 0 <= n_j < n:
                            res[i][j] += M[n_i][n_j]
                            count += 1
                res[i][j] //= count

        return res