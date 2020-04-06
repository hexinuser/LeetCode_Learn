# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 22:31:15 2018

@author: Evan_He
"""

class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        for i in range(1,n+1):
            t1,t2 = i%3,i%5
            if not(t1 or t2):
                res.append("FizzBuzz")
            elif not t1:
                res.append("Fizz")
            elif not t2:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res