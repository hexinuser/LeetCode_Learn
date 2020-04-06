# -*- coding: utf-8 -*-
"""
Created on Tue May  7 13:00:53 2019

@author: Evan_He
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走不就行了吗？即C(m+n-2,m-1)"""
        """
        res = 1
        res2 = 1
        for i in range(m-1):
            res *= m+n-2-i
        for i in range(1,m):
            res //= i
        return res
    
        """#动态规划
        dp = [[1 for _ in range(n)] for _ in range(m)] 
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
