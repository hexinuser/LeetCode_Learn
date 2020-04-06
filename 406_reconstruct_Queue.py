# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 21:09:16 2019

@author: Evan_He
"""

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        people = sorted(people,key = lambda x: (x[0],-x[1]),reverse = True)
        for i in range(1,len(people)):
            j =  people[i][1]
            while j != 0:
                people[i-j], people[i-j+1:i+1] = people[i],people[i-j:i]
                break
        return people[::-1]
        """
        """
        res = sorted(people,key = lambda x: (x[0],-x[1]))
        n = len(res)
        for i in range(2,n+1):
            j =  res[-i][1]
            if j != 0:
                if -i+j+1 !=0:
                    res[-i+j], res[-i:-i+j] = res[-i],res[-i+1:-i+j+1]
                else:
                    res[-i+j], res[-i:-i+j] = res[-i],res[-i+1:]
        return res
        """
        people.sort(key = lambda x: (-x[0],x[1]))
        res = []
        for per in people:
            res.insert(per[1],per)
        return res
        